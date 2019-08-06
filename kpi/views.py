from django.shortcuts import render
from rest_framework import status
from .models import *
from .serializer import ThemeticSerializer,IndicatorSerializer,Themetic_Indicators_DetailSerializer,Indicator_Target_Detail_Serializer,FinancialYearsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters

# Create your views here.

#view for the Themetics model
class Themetics_list(APIView):
    '''list of all the themetics '''
    def get(self,request):
        themetic=Themetics.objects.all()
        serializer_class=ThemeticSerializer(themetic,many=True)
        return Response({"Themetic list":serializer_class.data})
    
    def post(self, request):  # for adding a themetic
        seriliazer_class = ThemeticSerializer(data=request.data)
        if seriliazer_class.is_valid():
            seriliazer_class.save()
            return Response({"status": "Themetic {}   sucessfully created".format(seriliazer_class.data["themeticname"])}, status=201)
        else:
            return Response(seriliazer_class.errors)

class Indicators_list(APIView):
    '''list of all the themetics '''
    def get(self,request):
        indicators=Indicators.objects.all()
        serializer_class=IndicatorSerializer(indicators,many=True)
        return Response({"Indicators list":serializer_class.data})
    
    def post(self, request):  # for adding a themetic
        seriliazer_class = IndicatorSerializer(data=request.data)
        if seriliazer_class.is_valid():
            seriliazer_class.save()
            return Response({"status": "Indicator {}  sucessfully created".format(seriliazer_class.data["indicatorname"])}, status=201)
        else:
            return Response(seriliazer_class.errors)

class Financial_year_list(APIView):
    def get(self,request):
        financialyear=FinancialYears.objects.all()
        serializer_class=FinancialYearsSerializer(financialyear,many=True)
        return Response({"financial years list":serializer_class.data}) 
    def post(self,request):
        serializer_class=FinancialYearsSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            serializer_class.save()
            return Response({"new financial  {} year created ".format(serializer_class.data["year"])})
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)




class Themetic_Indicator_list(APIView):
    def get(self,request):
        themetic_indicator_list=Themetics.objects.all()
        serializer_class=Themetic_Indicators_DetailSerializer(themetic_indicator_list,many=True)
        return Response({"Themetic list":serializer_class.data})



class Indicator_Target_details(APIView):
    def get(self,request):
        indicator_targets=Indicators.objects.all()
        serializer_class=Indicator_Target_Detail_Serializer(indicator_targets,many=True)
        return Response({"Indicators Target Details":serializer_class.data})
    def  post(self,request):
        serializer=Indicator_Target_Detail_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"new {}  Indicators details created".format(serializer.data["indicatorname"])})
        else:
            return Response(serializer.errors)
        



    