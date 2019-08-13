from rest_framework import serializers
from .models import Farmers,LandDetails

""" Creating a serilizers for the models of the App farmer so data from the data base can be serialized in json data type"""

class FarmerSerializer(serializers.ModelSerializer):
    class Mata:
        model=Farmers
        fields="__all__"


class LandDetailsSerializer(serializers.ModelSerializer):
    class Mata:
        model=LandDetails
        fields="__all__"