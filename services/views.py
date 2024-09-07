from django.shortcuts import render
from rest_framework import viewsets
from services.serializer import ServiceSerializer
from services.models import Service


# Create your views here.
class ServiceView(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer

    #usar modelo a traves del orm
    queryset = Service.objects.all()
