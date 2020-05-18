from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *

class NPEquipmentSerializer(ModelSerializer):

    class Meta:
        model = NPEquipment
        exclude = ('discount', 'is_hourly',)

class NPSportSerializer(ModelSerializer):

    class Meta:
        model = NPSport
        fields = '__all__'


class NPSportInformationSerializer(ModelSerializer):
    sport = NPSportSerializer()

    class Meta:
        model = NPSportInformation
        fields = '__all__'
