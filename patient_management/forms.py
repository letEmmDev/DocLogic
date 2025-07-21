# forms.py
from django import forms
from .models import Patient

class PatientsForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['patient_surgeries', 'patient_info', 'patient_medications', 'patient_social_history']