from django.contrib import admin
from .models import Table

class sadmin(admin.ModelAdmin):
    list_display=('Title_of_activity','')
admin.site.register(Table,sadmin)
