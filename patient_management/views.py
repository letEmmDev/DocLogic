from django.shortcuts import render, get_object_or_404
# Create your views here.

from .models import Patient 
from hospital.models import Department
from rest_framework import viewsets
from .serializers import PatientReportSerializer
from .forms import PatientsForm

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

## Patient Report ViewSet
class PatientReportViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientReportSerializer

def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, patient_id=patient_id)
    return render(request, "patient_management/edit_patient.html", {"patient": patient})

## Partials for modal in the edit report page
def patient_info_form(request, patient_id):
    patient = get_object_or_404(Patient, patient_id=patient_id)
    return render(request, "patient_management/partials/patient_info_form.html", {"patient": patient})

def patient_medications_form(request, patient_id):
    patient = get_object_or_404(Patient, patient_id=patient_id)
    return render(request, "patient_management/partials/patient_medications_form.html", {"patient": patient})

def patient_surgeries_form(request, patient_id):
    patient = get_object_or_404(Patient, patient_id=patient_id)
    return render(request, "patient_management/partials/patient_surgeries_form.html", {"patient": patient})

def patient_social_history_form(request, patient_id):
    patient = get_object_or_404(Patient, patient_id=patient_id)
    return render(request, "patient_management/partials/patient_social_history_form.html", {"patient": patient})

def patients_form(request, patient_id):
    patient = get_object_or_404(Patient, patient_id=patient_id)
    form = PatientsForm(instance=patient)
    return render(request, "patient_management/partials/patient_surgeries_form.html", {"form": form, "patient": patient})