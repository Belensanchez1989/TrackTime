from django.shortcuts import render
from rest_framework import viewsets
from users.serializer import UserSerializer
from users.models import User


# Create your views here.
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    #usar modelo a traves del orm
    queryset = User.objects.all()
