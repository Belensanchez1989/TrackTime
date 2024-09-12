from django.shortcuts import render
from rest_framework import viewsets
from reservations.serializer import ReservationSerializer
from reservations.models import Reservation


# Create your views here.
class ReservationView(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer

    #usar modelo a traves del orm
    queryset = Reservation.objects.all()

