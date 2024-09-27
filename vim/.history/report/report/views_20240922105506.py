from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from service.models import Table
import uuid
from django.http import HttpResponseRedirect
def initialize_session(request):
    # Check if 'spp' is not already in the session
    if 'spp' not in request.session:
        # Generate a new unique identifier and store it in the session
        request.session['spp'] = str(uuid.uuid4())
    return request.session['spp']
def clear_spp(request):
    """
    Clear the 'spp' value from the session.
    """
    if 'spp' in request.session:
        del request.session['spp']
        
    return render(request, 'Buildinfo.html')


def Buildinfo(request):
    spp = initialize_session(request)
    return render(request, 'Buildinfo.html', {'spp': spp})
    