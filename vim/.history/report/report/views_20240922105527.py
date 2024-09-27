from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from reports.models import Table
import uuid
from django.http import HttpResponseRedirect


def Buildinfo(request):
    spp = initialize_session(request)
    return render(request, 'Buildinfo.html', {'spp': spp})
    