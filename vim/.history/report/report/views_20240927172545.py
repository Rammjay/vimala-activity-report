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
            
            Title_of_activity = request.POST.get('toa')
            department=request.POST.get('dept')
            nature=request.POST.get('nat')
            date=request.POST.get('date')
            resource_person=request.POST.get('rp')
            brief_report=request.POST.get('br')
            collaborating_units=request.POST.get('colu')
            funded_by=request.POST.get('fund')
            no_of_participants=request.POST.get('nop')
            faculty_coordinator=request.POST.get('fco')
            student_coordinator=request.POST.get('sco')            
            
            en = Table.objects.filter(Title_of_activity=Title_of_activity).first()

            if en:
                if Title_of_activity:
                    en.Title_of_activity = Title_of_activity
                if department:
                    en.department=department
                if nature:
                    en.nature=nature
                if date:
                    en.date=date
                if resource_person:
                    en.resource_person=resource_person
                if brief_report:
                    en.brief_report=brief_report
                
                
                   
                
                
                en.save()
            else:
                # If no entry exists, create a new one
                en = Table(
                    
                    Title_of_activity=Title_of_activity,
                    

                )
            en.save()
            return redirect('main')
        except Exception as e:
            print("Error saving data:", e)
        return HttpResponseRedirect("main")
    return redirect('main')
    