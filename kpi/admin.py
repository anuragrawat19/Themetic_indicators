from django.contrib import admin

from .models import (
    Indicators,
    Themetics,
    FinancialYears,
    IndicatorTargets)

# Register your models here.
admin.site.register(Indicators)
admin.site.register(Themetics)
admin.site.register(FinancialYears)
admin.site.register(IndicatorTargets)
