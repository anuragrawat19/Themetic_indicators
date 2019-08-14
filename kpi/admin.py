from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import (
    Indicators,
    Themetics,
    FinancialYears,
    IndicatorTargets,
    IndicatorTargetAchievements,Urban)

# Register your models here.
admin.site.register(Indicators)
admin.site.register(Themetics)
admin.site.register(FinancialYears)
admin.site.register(IndicatorTargets)

@admin.register(IndicatorTargetAchievements)
class ViewAdmin(ImportExportModelAdmin):
    pass


@admin.register(Urban)
class UrbanView(ImportExportModelAdmin):
    pass
