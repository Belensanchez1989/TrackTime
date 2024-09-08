from rest_framework import serializers
from .models import Day, Month, Year


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day

        # serializacion de la data
        fields = "__all__"


class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Month

        # serializacion de la data
        fields = "__all__"


class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year

        # serializacion de la data
        fields = "__all__"
