from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from reports.models import Table
import uuid
from django.http import HttpResponseRedirect

def main(request):
    
    return render(request, '1.html')

