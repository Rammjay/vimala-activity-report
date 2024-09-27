from django.db import models    
import re
from django.core.exceptions import ValidationError

class Table(models.Model):
    btype = models.CharField(max_length=35, null=True, blank=True)
    spp = models.CharField(max_length=1000, null=True, blank=True)
    
    # Number fields for the form

    flb1 = models.IntegerField(null=True, blank=True)
    flb2 = models.IntegerField(null=True, blank=True)
    flb3 = models.IntegerField(null=True, blank=True)
    flb4 = models.IntegerField(null=True, blank=True)
    
    slb1 = models.IntegerField(null=True, blank=True)
    slb2 = models.IntegerField(null=True, blank=True)
    slb3 = models.IntegerField(null=True, blank=True)
    slb4 = models.IntegerField(null=True, blank=True)
    
    flnb1 = models.IntegerField(null=True, blank=True)
    flnb2 = models.IntegerField(null=True, blank=True)
    flnb3 = models.IntegerField(null=True, blank=True)
    flnb4 = models.IntegerField(null=True, blank=True)
    
    slnb1 = models.IntegerField(null=True, blank=True)
    slnb2 = models.IntegerField(null=True, blank=True)
    slnb3 = models.IntegerField(null=True, blank=True)
    slnb4 = models.IntegerField(null=True, blank=True)
    
    # References
    sprd = models.DateField(null=True, blank=True)
    Dooc = models.CharField(max_length=25, null=True)
    Priority = models.CharField(
        max_length=10,
        choices=[('Emergency', 'Emergency'), ('Urgent', 'Urgent'), ('Routine', 'Routine')],
        default='Emergency',
        null=True,
         

    )
    sprno = models.CharField(max_length=25, null=True)
    memono = models.CharField(max_length=25, null=True)
    project = models.CharField(max_length=25, null=True)
    subsystem = models.CharField(max_length=25, null=True)

    #Problems

    pct=models.TextField(max_length=1000,default="",null=True)
    pcd=models.TextField(max_length=1000,default="",null=True)

    # Stakeholders
    Assigned_to = models.CharField(max_length=25, null=True)
    Initiated_by = models.CharField(max_length=25, null=True)
    Approved_by = models.CharField(max_length=25, null=True )

    #constant
    tstring=models.TextField(max_length=10000,default=" ",null=True)

    clawstring=models.TextField(max_length=10000,default=" ",null=True)

    Rstring=models.TextField(max_length=10000,default=" ",null=True)



    def clean(self):
        super().clean()
        if self.sprno and not re.match(r'^[A-Z0-9/_]+$', self.sprno):
            raise ValidationError({'sprno': 'Invalid characters in SPR No.'})

    def __str__(self):
        return " "
