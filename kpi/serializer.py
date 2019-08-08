'''Wrting a seriliazers for the models so that state of 
the model objects can be converted into a native python datatypes like json,xml '''
from rest_framework import serializers
from .models import (Themetics,Indicators,FinancialYears,IndicatorTargets,IndicatorTargetAchievements)

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


class IndicatorTargetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=IndicatorTargets
        fields=["financialyear","quarter","target"]

class Indicator_Target_Detail_Serializer(serializers.ModelSerializer):
    indicator_target=IndicatorTargetModelSerializer(many=True)
    class Meta:
        model=Indicators
        fields=["id","themetic","indicatorname","shortcode","indicator_target"]


  #Using Serialzer for serialization
#----------------------------------------------------------------------------------

class IndicatorTargetCoustomSerializer(serializers.Serializer):
    QUARTER = (
    (1, "Quarter 1"),
    (2, "Quarter 2"),
    (3, "Quarter 3"),
    (4, "Quarter 4")
    )
    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField()
    modified = serializers.DateTimeField()
    ACTIVE_CHOICES = ((0, 'Inactive'), (1, 'Active'))
    active = serializers.ChoiceField(choices=ACTIVE_CHOICES, default=1)
    indicator=serializers.PrimaryKeyRelatedField(read_only=True)
    indicatorname=serializers.SerializerMethodField("indicator_name")
    financialyear = serializers.CharField(max_length=50)
    quarter=serializers.ChoiceField(choices=QUARTER)
    target = serializers.IntegerField()

    def indicator_name(self,obj):
        return obj.indicator.indicatorname

    def create(self,validated_data):
        indicators=validated_data.pop("indicator")
        year=validated_data.pop("financialyear")
        Indicators_id=Indicators.objects.get(id=indicators)
        year=FinancialYears.objects.get(year=year)
        return IndicatorTargets.objects.create(indicator=Indicators_id,financialyear=year,**validated_data)




class IndicatorTargetAchievementSerializer(serializers.Serializer):
    themetic=serializers.SerializerMethodField("Themetic",read_only=True)
    achievedtarget=serializers.PrimaryKeyRelatedField(read_only=True)
    Indicator_target_name=serializers.SerializerMethodField("targetname",read_only=True)
    year= serializers.SerializerMethodField("Year",read_only=True)
    quarter = serializers.SerializerMethodField("Quarter",read_only=True)
    target = serializers.SerializerMethodField("Target",read_only=True)
    def targetname(self,obj):
        return obj.achievedtarget.indicator.indicatorname
    
    def Target(self,obj):
        return obj.achievedtarget.target
    
    def Themetic(self,obj):
        return obj.achievedtarget.indicator.themetic.themeticname
    
    def Year (self,obj):
        return obj.achievedtarget.financialyear.year
    
    def Quarter(self,obj):
        return obj.achievedtarget.quarter

    def create(self,validated_data):
        Indicator_Target=validated_data.pop("achievedtarget")
        target_instance=IndicatorTargets.objects.get(id=Indicator_Target)
        return IndicatorTargetAchievements.objects.create(achievedtarget=target_instance)
    
    def update(self,instance,validated_data):
        instance.achievedtarget=validated_data.get("achievedtarget",instance.achievedtarget)
        instance.save()
        return instance

    





