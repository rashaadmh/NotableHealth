import json

from django.http import JsonResponse, HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
import datetime
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from doctor.models import Doctor, Appointment


def get_doctors(request):
    doctors = Doctor.objects.all()
    json_response = {}
    for doctor in doctors:
        json_response[str(doctor.uuid)] = {'first_name': doctor.first_name,
                                           'last_name': doctor.last_name,
                                           'uuid': str(doctor.uuid)}
    return JsonResponse(json_response)


def get_appointment_for_doctor(request):
    doctor_uuid = request.GET.get('doctor_uuid', None)
    date_str = request.GET.get('date', None) # should be in format "%Y-%m-%d"
    if not date_str:
        return HttpResponseBadRequest('Must provide date')
    if not doctor_uuid:
        return HttpResponseBadRequest('Must provide doctor_uuid')
    doctor = Doctor.objects.get(uuid=doctor_uuid)
    if not doctor:
        return HttpResponseNotFound('No Doctor Found')

    date = datetime.datetime.strptime(date_str, '%Y-%m-%d')

    appointments = doctor.appointment_set.all()
    appointments = appointments.filter(date__date=date)
    result_set = {}
    for appointment in appointments:
        result_set[str(appointment.uuid)] = {'patient_first_name': appointment.patient_first_name,
                                             'patient_last_name': appointment.patient_last_name,
                                             'date': appointment.date,
                                             'kind': appointment.kind,
                                             'uuid': appointment.uuid}

    return JsonResponse(result_set)


def delete_appointment(request):
    appointment_uuid = request.GET.get('appointment_uuid', None)
    if not appointment_uuid:
        return HttpResponseBadRequest('Must provide appointment uuid')
    appointment = Appointment.objects.get(uuid=appointment_uuid)
    if not appointment:
        return HttpResponseNotFound('Appointment not found')
    appointment.delete()
    return HttpResponse(200)


@csrf_exempt
def create_appointment(request):
    body = json.loads(request.body)
    doctor_uuid = body['doctor_uuid']
    datetime_str = body['datetime']
    patient_first_name = body['patient_first_name']
    patient_last_name = body['patient_last_name']
    kind = body['kind']
    date_object = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
    date_minute = date_object.minute
    if date_minute not in [0, 15, 30, 45]:
        return HttpResponseBadRequest('Time must be at a 15 minute interval of the hour')
    doctor = Doctor.objects.get(uuid=doctor_uuid)
    if not doctor:
        return HttpResponseNotFound('Doctor not found')
    appointments = doctor.appointment_set.filter(date=date_object)

    if len(appointments) < 3:
        Appointment.objects.create(patient_first_name=patient_first_name, patient_last_name=patient_last_name,
                                   date=date_object, kind=kind, doctor=doctor)
        return HttpResponse(200)
    else:
        return HttpResponse(406)

@csrf_exempt
def create_doctor(request):
    body = json.loads(request.body)
    first_name = body['first_name']
    last_name = body['last_name']

    doctor = Doctor.objects.create(first_name=first_name, last_name=last_name)
    return HttpResponse(200)