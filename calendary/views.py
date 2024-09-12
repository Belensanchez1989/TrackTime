from django.shortcuts import render
from rest_framework import viewsets
from calendary.serializer import DaySerializer, MonthSerializer, YearSerializer
from .models import Day, Month, Year


class DayViewSet(viewsets.ModelViewSet):
    serializer_class = DaySerializer

    queryset = Day.objects.all()


class MonthViewSet(viewsets.ModelViewSet):
    serializer_class = MonthSerializer

    queryset = Month.objects.all()


class YearViewSet(viewsets.ModelViewSet):
    serializer_class = YearSerializer

    queryset = Year.objects.all()
