from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("devices/", views.DevicesAPI.as_view(), name='devices'),
    path("devices/<str:uid>", views.DeviceAPI.as_view(), name='device'),
    path("devices/<str:uid>/readings/<str:parameter>/",
         views.DeviceReadingAPI.as_view(), name="readings"),
]
