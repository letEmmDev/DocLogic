from rest_framework import serializers
from .models import Patient

class PatientReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['patient_id', 'patient_info', 'patient_medications', 'patient_surgeries', 'patient_social_history']