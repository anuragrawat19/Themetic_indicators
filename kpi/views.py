from django.shortcuts import render
from rest_framework import status
from .models import *
from .serializer import (ThemeticSerializer, IndicatorSerializer, Themetic_Indicators_DetailSerializer,
                         Indicator_Target_Detail_Serializer, FinancialYearsSerializer, IndicatorTargetCoustomSerializer, IndicatorTargetAchievementSerializer)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters

# Create your views here.

# view for the Themetics model


class Themetics_list(APIView):
    '''list of all the themetics '''

    def get(self, request):
        themetic = Themetics.objects.all()
        serializer_class = ThemeticSerializer(themetic, many=True)
        return Response({"Themetic list": serializer_class.data})

    def post(self, request):  # for adding a themetic
        seriliazer_class = ThemeticSerializer(data=request.data)
        if seriliazer_class.is_valid():
            seriliazer_class.save()
            return Response({"status": "Themetic {}   sucessfully created".format(seriliazer_class.data["themeticname"])}, status=201)
        else:
            return Response(seriliazer_class.errors)


class Themetic_Update_Delete(APIView):
    def put(self, request, themetic_id):
        themetic = Themetics.objects.get(pk=themetic_id)
        serializer_class = ThemeticSerializer(themetic, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({"status": " Themetic {} is update ".format(themetic.themeticname)})
        else:
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, themetic_id):
        try:
            themetic = Themetics.objects.get(pk=themetic_id)
            themetic.delete()
            return Response({" {} themetic is deleted ".format(themetic.themeticname)})
        except Themetics.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Indicators_list(APIView):
    '''list of all the themetics '''

    def get(self, request):
        indicators = Indicators.objects.all()
        serializer_class = IndicatorSerializer(indicators, many=True)
        return Response({"Indicators list": serializer_class.data})

    def post(self, request):  # for adding a themetic
        seriliazer_class = IndicatorSerializer(data=request.data)
        if seriliazer_class.is_valid():
            seriliazer_class.save()
            return Response({"status": "Indicator {}  sucessfully created".format(seriliazer_class.data["indicatorname"])}, status=201)
        else:
            return Response(seriliazer_class.errors)


class Indicator_Update_Delete(APIView):

    def put(self, request, indicator_id):
        indicator = Indicators.objects.get(id=indicator_id)
        serializer_class = IndicatorSerializer(indicator, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response("existing indicator '{1}' of id {0} modified".format(serializer_class.data["id"], indicator.indicatorname))
        else:
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, indicator_id):
        try:
            indicator = Indicators.objects.get(id=indicator_id)
            indicator.delete()
            return Response({"indicator {1} with id {0} is deleted".format(indicator_id, indicator.indicatorname)})
        except Indicators.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Financial_year_list(APIView):
    def get(self, request):
        financialyear = FinancialYears.objects.all()
        serializer_class = FinancialYearsSerializer(financialyear, many=True)
        return Response({"financial years list": serializer_class.data})

    def post(self, request):
        serializer_class = FinancialYearsSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            serializer_class.save()
            return Response({"new financial  {} year created ".format(serializer_class.data["year"])})
        else:
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, year_id):
        year = FinancialYears.objects.get(id=year_id)
        serializer_class = FinancialYearsSerializer(year, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response("existing year with id {0} modified".format(serializer_class.data["id"], year.year))
        else:
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, year_id):
        try:
            year = FinancialYears.objects.get(id=year_id)
            year.delete()
            return Response({"year  {1} with id {0} is deleted".format(year_id, year.year)})
        except Indicators.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Themetic_Indicator_list(APIView):
    def get(self, request):
        themetic_indicator_list = Themetics.objects.all()
        serializer_class = Themetic_Indicators_DetailSerializer(
            themetic_indicator_list, many=True)
        return Response({"Themetic list": serializer_class.data})


class Indicator_Target_details(APIView):
    def get(self, request):
        indicator_targets = Indicators.objects.all()
        serializer_class = Indicator_Target_Detail_Serializer(
            indicator_targets, many=True)
        return Response({"Indicators Target Details": serializer_class.data})

    def post(self, request):
        serializer = Indicator_Target_Detail_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"new {}  Indicators details created".format(serializer.data["indicatorname"])})
        else:
            return Response(serializer.errors)
# ---------------------------------------------------------------


class IndicatorTargetList(APIView):
    def get(self, request):
        IndicatorTargetList = IndicatorTargets.objects.all()
        seriliazer_class = IndicatorTargetCoustomSerializer(
            IndicatorTargetList, many=True)
        return Response({"Indicators Target List": seriliazer_class.data})

    def post(self, request):
        IndicatorTargetList = IndicatorTargetCoustomSerializer(
            data=request.data)
        if IndicatorTargetList.is_valid(raise_exception=True):
            IndicatorTargetList.save()
            return Response({"status": "New Indicator target is created  "}, status=status.HTTP_201_CREATED)
        else:
            return Response(IndicatorTargetList.ValidationError)

# ---------------------------------------------------------------------


class AchievedTargets(APIView):
    def get(self, request):
        achieved_targets = IndicatorTargetAchievements.objects.all()
        serializer_class = IndicatorTargetAchievementSerializer(
            achieved_targets, many=True)
        return Response({"achieved targets": serializer_class.data})

    def post(self, request):
        serializer_class = IndicatorTargetAchievementSerializer(
            data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({" status": " new indicator target is achived"})
        else:
            return Response(serializer_class.errors)

   
    def put(self, request, achieved_target_id):
        achieved_targets = IndicatorTargetAchievements.objects.get(achievedtarget=achieved_target_id)
        serializer_class = IndicatorTargetAchievementSerializer(achieved_targets, request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response("existing target with id {} modified".format(achieved_target_id))
        else:
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, achieved_target_id):
        try:
            achieved_targets = IndicatorTargetAchievements.objects.get(achievedtarget=achieved_target_id)
            achieved_targets.delete()
            return Response({"achieved target  with id {} is deleted".format(achieved_target_id)})
        except IndicatorTargetAchievements.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
