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
    url(r'^themetic-list/$',views.Themetics_list.as_view()),
    url(r'^themetic-list/(?P<themetic_id>[0-9]+)/$',views.Themetic_Update_Delete.as_view()),
    url(r'^indicators-list/$',views.Indicators_list.as_view()),
    url(r'^indicators-list/(?P<indicator_id>[0-9]+)/$',views.Indicator_Update_Delete.as_view()),
    url(r'^financialyears-list/$',views.Financial_year_list.as_view()),
    url(r'^financialyears-list/(?P<year_id>[0-9]+)/$',views.Financial_year_list.as_view()),
    url(r'^themetic-indicator-list/$',views.Themetic_Indicator_list.as_view()),
    url(r'^indicator-targetsdetails/$',views.Indicator_Target_details.as_view()),
    url(r'^indicatortarget-list/$',views.IndicatorTargetList.as_view()),
    url(r'^achievedtarget-list/$',views.AchievedTargets.as_view()),
    url(r'^achievedtarget-list/achieved-day-details/$', views.AchievedTargets_period_info.as_view()),
    url(r'^achievedtarget-list/(?P<achieved_target_id>[0-9]+)/$',views.AchievedTargets.as_view()),
    url(r'^achievedtarget-list/search/(?P<year>[\w\s-]+)/$',views.Year_Based_AchievedTarget.as_view()),
    




]

