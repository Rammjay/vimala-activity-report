from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from reports.models import Table
import uuid
from django.http import HttpResponseRedirect


def main(request):
    
    return render(request, '1.html')
def Submit(request):
    if request.method == "POST":
        print("Form Data Received:", request.POST)  # Log all POST data

        try:
            # Extract POST data
            
            Time_of_activity = request.POST.get('toa')
            
            
            en = Table.objects.filter(toa=toa).first()

            if en:
                if Title_of_activity:
                    en.toa = toa
                   
                
                
                en.save()
            else:
                # If no entry exists, create a new one
                en = Table(
                    
                    toa=Title_of_activity,
                    

                )
            en.save()
            return redirect('main')
        except Exception as e:
            print("Error saving data:", e)
        return HttpResponseRedirect("main")
    return redirect('main')
    