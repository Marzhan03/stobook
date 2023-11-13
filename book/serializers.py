from rest_framework import serializers
from . import models


class CardTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cardtype
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = '__all__'

class StreetSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    class Meta:
        model = models.Street
        fields = [
            'id',
            'street',
            'city'
        ]