from django.db import models

# Create your models here.
from django.db import models
import uuid
from datetime import datetime


class Doctor(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)


class Appointment(models.Model):
    NEW_PATIENT = 'new_patient'
    FOLLOW_UP = 'follow_up'
    KIND_CHOICES = (
        (NEW_PATIENT, 'new_patient'),
        (FOLLOW_UP, 'follow_up')
    )

    uuid = models.UUIDField(db_index=True, default=uuid.uuid4)
    patient_first_name = models.CharField(max_length=50)
    patient_last_name = models.CharField(max_length=50)
    date = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    kind = models.CharField(max_length=50, choices=KIND_CHOICES)
