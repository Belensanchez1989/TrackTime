from rest_framework import serializers
from hours.models import Hour


class HourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hour

        # serializacion de la data
        fields = "__all__"
