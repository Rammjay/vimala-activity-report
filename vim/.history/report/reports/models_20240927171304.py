from django.db import models    
import re
from django.core.exceptions import ValidationError

class Table(models.Model):
    Title_of_activity =models.CharField(max_length=100,null=True)
    department = models.CharField(max_length=100,null=True)
    nature = models.CharField(max_length=100,null=True)
    date = models.CharField(max_length=100,null=True)
    resource_person = models.CharField(max_length=100,null=True)
    brief_report = models.TextField(max_length=100,null=True)
    collaborating_ = models.CharField(max_length=100,null=True)
    fund = models.CharField(max_length=100,null=True)
    nop = models.CharField(max_length=100,null=True)
    fco = models.CharField(max_length=100,null=True)
    sco = models.CharField(max_length=100,null=True)
    


    def __str__(self):
        return " "
