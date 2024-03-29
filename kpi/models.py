from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError


class BaseContent(models.Model):
    ACTIVE_CHOICES = ((0, 'Inactive'), (1, 'Active'))
    active = models.PositiveIntegerField(choices=ACTIVE_CHOICES, default=1)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class Themetics(BaseContent):
    themeticname = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "themetics"
        verbose_name_plural = "Themetics"
        ordering = ['id']

    def __str__(self):
        return self.themeticname


class Indicators(BaseContent):
    indicatorname = models.CharField(max_length=100)
    shortcode = models.CharField(max_length=20)
    themetic = models.ForeignKey(
        Themetics, related_name="theme", on_delete=models.CASCADE)

    class Meta:
        db_table = "indicators"
        verbose_name_plural = "Indicators"
        ordering = ["id"]

    def __str__(self):
        return self.indicatorname


class FinancialYears(BaseContent):
    year = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = "financialyear"
        verbose_name_plural = "Financial Years"
        ordering = ["year"]

    def __str__(self):
        return self.year


QUARTER = (
    (1, "Quarter 1"),
    (2, "Quarter 2"),
    (3, "Quarter 3"),
    (4, "Quarter 4")
)


class IndicatorTargets(BaseContent):
    indicator = models.ForeignKey(
        Indicators, related_name="indicator_target", on_delete=models.CASCADE)
    financialyear = models.ForeignKey(
        FinancialYears, related_name="finance_year")
    quarter = models.IntegerField(choices=QUARTER, default=1)
    target = models.PositiveIntegerField()


    class Meta:
        db_table = "indicatortargets"
        verbose_name_plural = "IndicatorTargets"

    def __str__(self):
        return str(self.indicator)
    
class IndicatorTargetAchievements(BaseContent):
    indicatortarget = models.OneToOneField(IndicatorTargets,primary_key=True,related_name="target_achieved")
    achievedtarget = models.PositiveIntegerField()
    


    class Meta:
        db_table="indicatortargetachievements"
    
    def __str__(self):
        return str(self.indicatortarget.indicator.indicatorname)


class Userslist(BaseContent):
    user=models.CharField(max_length=30)
    username=models.CharField(max_length=50)
    firstname=models.CharField(max_length=50,null=True,blank=True)
    lastname=models.CharField(max_length=50,null=True,blank=True)
    roleid=models.IntegerField()
    roletype=models.CharField(max_length=50)

    def __str__(self):
        return self.user

    class Meta:
        db_table="users"


class Urban(BaseContent):
    country=models.CharField(max_length=50)
    state=models.CharField(max_length=40)
    district=models.CharField(max_length=60)
    city=models.CharField(max_length=100)
    area=models.CharField(max_length=100)
    ward=models.CharField(max_length=30,null=True,blank=True)
    mohala=models.CharField(max_length=50)
    geographicalarea=models.CharField(max_length=60)

    class Meta:
        db_table="urban"
    
    
    def __str__(self):
        return self.state