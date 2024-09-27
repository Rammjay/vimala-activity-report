from django.contrib import admin
from .models import Table

class sadmin(admin.ModelAdmin):
    list_display=('btype)
admin.site.register(Table,sadmin)
