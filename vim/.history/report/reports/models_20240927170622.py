from django.db import models    
import re
from django.core.exceptions import ValidationError

class Table(models.Model):
    toa=models.CharField(max_length=100,null=True)
    nat = models.CharField(max_length=100,null=True)
    date = models.CharField(max_length=100,null=True)
    dept = models.CharField(max_length=100,null=True)
    br = models.TextField(max_length=100,null=True)
    rp = models.CharField(max_length=100,null=True)
    colu = models.CharField(max_length=100,null=True)
    fund = models.CharField(max_length=100,null=True)
    nop = models.CharField(max_length=100,null=True)
    fco = document.getElementById('fco').value;
    sco = document.getElementById('sco').value;
    


    def __str__(self):
        return " "
