from django.db import models


class Sample(models.Model):
    field1 = models.CharField(max_length=30)
    field2 = models.CharField(max_length=30)
