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
    collaborating_units = models.CharField(max_length=100,null=True)
    funded_by = models.CharField(max_length=100,null=True)
    no_of_participants = models.CharField(max_length=100,null=True)
    faculty_coordinator = models.CharField(max_length=100,null=True)
    student_coordinator = models.CharField(max_length=100,null=True)
    
    


    def __str__(self):
        return " "
