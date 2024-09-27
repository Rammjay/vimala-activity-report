from django.contrib import admin
from .models import Table

class sadmin(admin.ModelAdmin):
    list_display=('Assigned_to','Initiated_by','Approved_by')
admin.site.register(Table,sadmin)
