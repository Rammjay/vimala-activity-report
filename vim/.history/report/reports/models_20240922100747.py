from django.db import models    
import re
from django.core.exceptions import ValidationError

class Table(models.Model):
    name
    btype = models.CharField(max_length=35, null=True, blank=True)
    spp = models.CharField(max_length=1000, null=True, blank=True)
    


    def __str__(self):
        return " "
