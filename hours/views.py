from django.shortcuts import render
from rest_framework import viewsets
from hours.serializer import HourSerializer
from hours.models import Hour


# Create your views here.
class HourView(viewsets.ModelViewSet):
    serializer_class = HourSerializer

    #usar modelo a traves del orm
    queryset = Hour.objects.all()
# Create your views here.
