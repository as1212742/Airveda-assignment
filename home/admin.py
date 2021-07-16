from django.contrib import admin
from home.models import *

# Register your models here.
admin.site.register(Devices)
admin.site.register(TemperatureReading)
admin.site.register(HumidityReading)
