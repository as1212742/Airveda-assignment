from rest_framework import serializers
from .models import *


class DevicesSerialisers(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = '__all__'


class TemperatureSerialisers(serializers.ModelSerializer):
    class Meta:
        model = TemperatureReading
        fields = '__all__'


class HumiditySerialisers(serializers.ModelSerializer):
    class Meta:
        model = HumidityReading
        fields = '__all__'
