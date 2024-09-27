from django.db import models    
import re
from django.core.exceptions import ValidationError

class Table(models.Model):
    n=models.CharField(max_length=100,null=True)
    


    def __str__(self):
        return " "
