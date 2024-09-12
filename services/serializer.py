from rest_framework import serializers
from services.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service

        # serializacion de la data
        fields = "__all__"
