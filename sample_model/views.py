from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
import requests


def test_view(request):
    p1 = request.GET.get('p1', None)
    p2 = request.GET.get('p2', None)
    json = {'responses': p1,
            'item': p2}
    return JsonResponse(json)

@csrf_exempt
def test_view_with_body(request):
    body = json.loads(request.body)
    json_data = {'result': body['body'],
                 'result2': body['second']}
    return JsonResponse(json_data)
