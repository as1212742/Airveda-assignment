from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from datetime import datetime

# Create your views here.


class DevicesAPI(APIView):
    """This represents Devices API"""

    def get(self, request):
        devices = Devices.objects.all()
        serializer = DevicesSerialisers(devices, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = DevicesSerialisers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class DeviceAPI(APIView):
    """This represents Device API"""

    def get(self, request, uid):
        devices = Devices.objects.get(uid=uid)
        serializer = DevicesSerialisers(devices, many=False)
        return Response(serializer.data)

    def delete(self, request, uid):
        devices = Devices.objects.get(uid=uid)
        messages = "Succesfully deleted!"
        devices.delete()
        return Response(messages)


class DeviceReadingAPI(APIView):
    """This represents Devices API"""

    def get(self, request, uid, parameter):
        start_on = request.GET.get('start_on')
        end_on = request.GET.get('end_on')

        start_on = datetime.strptime(start_on, "%Y-%m-%dT%H:%M:%S")
        end_on = datetime.strptime(end_on, "%Y-%m-%dT%H:%M:%S")

        if parameter == "temperature":
            devices = TemperatureReading.objects.filter(
                uid=uid, date__range=[start_on, end_on])
            serializer = TemperatureSerialisers(devices, many=True)
            return Response(serializer.data)

        elif parameter == "humidity":
            devices = HumidityReading.objects.filter(
                uid=uid, date__range=[start_on, end_on])
            serializer = HumiditySerialisers(devices, many=True)
            return Response(serializer.data)
