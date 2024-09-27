from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from service.models import Table
import uuid
from django.http import HttpResponseRedirect

def main(request):
    
    return render(request, '1.html')

def submit(request):
    if request.method == "POST":
        print("Form Data Received:", request.POST)  # Log all POST data

        try:
            # Extract POST data
            
            toa = request.POST.get('toa')
            
            
            print("Received tstring:", clawstring)  # Log tstring value
            # Look for an existing entry based on a unique identifier (sprno in this case)
            en = Table.objects.filter(toa=toa).first()

            if en:
                if toa:
                    en.toa = toa
                   
                
                
                en.save()
            else:
                # If no entry exists, create a new one
                en = Table(
                    
                    toa=toa,
                    

                )
            en.save()
            print("tstrings value:", tstring)
            return redirect(next_url)
        except Exception as e:
            print("Error saving data:", e)
        return HttpResponseRedirect("")
    return redirect('Buildinfo')