'''Wrting a seriliazers for the models so that state of 
the model objects can be converted into a native python datatypes like json,xml '''
from rest_framework import serializers
from .models import (Themetics,Indicators,FinancialYears,IndicatorTargets)

class ThemeticSerializer(serializers.ModelSerializer):
    class Meta:
        model=Themetics
        fields="__all__"

class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Indicators
        fields="__all__"

class FinancialYearsSerializer(serializers.ModelSerializer):
    class Meta:
        model=FinancialYears
        fields="__all__"

class Themetic_Indicators_DetailSerializer(serializers.ModelSerializer):
    indicators= serializers.SerializerMethodField("Themetic_indicators_list")

    def Themetic_indicators_list(self,obj):
        return obj.theme.all().values("indicatorname")
   
    class Meta:
        model=Themetics
        fields=["id","themeticname","code","indicators"]


#------------------------------------------------------------------------------


class IndicatorTargetSerializer(serializers.ModelSerializer):
    class Meta:
        model=IndicatorTargets
        fields=["financialyear","quarter","target"]

class Indicator_Target_Detail_Serializer(serializers.ModelSerializer):
    indicator_target=IndicatorTargetSerializer(many=True)
    class Meta:
        model=Indicators
        fields=["id","themetic","indicatorname","shortcode","indicator_target"]
        
    
    def create(self,validated_data):
        indicator_data=validated_data.pop('indicator_target')[0]
        Indicator=Indicators.objects.create(**validated_data)
        IndicatorTargets.objects.create(indicator=Indicator,**indicator_data)
        return Indicator



