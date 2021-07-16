from django.db import models
from rest_framework import serializers
import uuid

# Create your models here.


class Devices(models.Model):
    uid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TemperatureReading(models.Model):
    uid = models.ForeignKey(Devices, on_delete=models.CASCADE)
    temperature = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class HumidityReading(models.Model):
    uid = models.ForeignKey(Devices, on_delete=models.CASCADE)
    humidity = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
