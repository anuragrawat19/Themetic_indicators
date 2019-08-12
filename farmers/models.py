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
def contact_validator(value):
    if len(str(value))!=10:
        raise ValidationError(" Contact should contain 10 digits")
    
class Farmers(BaseContent):
    name=models.CharField(max_length=50,verbose_name="Farmer's name")
    age=models.IntegerField()
    Address=models.CharField(max_length=100)
    contactno=models.BigIntegerField(validators=[contact_validator])
    familymember=models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table="farmers"
        ordering=["id"]

class LandDetails(BaseContent):
    farmer = models.ForeignKey(
        Farmers, related_name="theme", on_delete=models.CASCADE)
    location=models.CharField(max_length=50)
    landarea=models.IntegerField(db_column="Land area in acers")
    annualproduction=models.IntegerField(db_column="Production in Tonnes")

    def __str__(self):
        return str(self.farmer)
    
    class Meta:
        db_table="landdetails"
        ordering=["farmer"]

