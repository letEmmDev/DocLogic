from django.shortcuts import render

# Create your views here.

from .models import Patient 
from hospital.models import Department

def patient_list(request):
    department_name = request.GET.get('department')
    if department_name and department_name != 'all':
        patients = Patient.objects.filter(department__name__iexact=department_name)
    else:
        patients = Patient.objects.all()
    departments = Department.objects.all()
    if request.htmx:
        # Return both fragments for HTMX requests
        return render(request, "patient_management/patient_cards.html", {
            "patients": patients,
            "departments": departments,
            "selected_department": department_name or "all"
        })
    # For full page load, also include count
    return render(request, "core/dashboard/dashboard_staff.html", {
        "patients": patients,
        "departments": departments,
    })