"""Themeticindicators URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from kpi import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^themetic_list/$',views.Themetics_list.as_view()),
    url(r'^indicators_list/$',views.Indicators_list.as_view()),
    url(r'^financialyears_list/$',views.Financial_year_list.as_view()),
    url(r'^themetic_indicator_list/$',views.Themetic_Indicator_list.as_view()),
    url(r'^indicator_targetsdetails/$',views.Indicator_Target_details.as_view()),


]

