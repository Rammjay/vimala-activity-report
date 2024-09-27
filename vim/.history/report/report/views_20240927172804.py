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
                if collaborating_units:
                    en.collaborating_units=collaborating_units
                if funded_by:
                    en.funded_by=funded_by
                if no_of_participants:
                    en.no_of_participants=no_of_participants
                if faculty_coordinator:
                    en.faculty_coordinator=faculty_coordinator
                if student_coordinator:
                    en.student_coordinator=student_coordinator
                
                   
                
                
                en.save()
            else:
                # If no entry exists, create a new one
                en = Table(
                    
                    Title_of_activity=Title_of_activity,
                    department=department,
                    nature=nature,
                    date=date,
                    resource_person=resource_person,
                    brief_report=brief_report,
                    collaborating_units=collaborating_units,
                    funded_by=funded_by,
                    no_of_participants=no_of_participants,
                    faculty_coordinator=faculty_coordinator,
                    

                )
            en.save()
            return redirect('main')
        except Exception as e:
            print("Error saving data:", e)
        return HttpResponseRedirect("main")
    return redirect('main')
    