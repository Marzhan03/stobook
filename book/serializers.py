from rest_framework import serializers
from . import models


class CardTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cardtype
        fields = '__all__'
