from django.db import models    
import re
from django.core.exceptions import ValidationError

class Table(models.Model):
    toa=models.CharField(max_length=100,null=True)
    nat = models.CharField(max_length=100,null=True)
    date = models.CharField(max_length=100,null=True)
    dept = models.CharField(max_length=100,null=True)
    br = document.getElementById('br').value;
    rp = document.getElementById('rp').value;
    colu = document.getElementById('colu').value;
    fund = document.getElementById('fund').value;
    nop = document.getElementById('nop').value;
    fco = document.getElementById('fco').value;
    sco = document.getElementById('sco').value;
    


    def __str__(self):
        return " "
