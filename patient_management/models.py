from django.db import models

# Create your models here.

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('core.CustomUser', on_delete=models.CASCADE, related_name='patient_profile')
    age = models.IntegerField()
    department = models.ForeignKey('hospital.Department', on_delete=models.CASCADE, related_name='patients')
    profile_picture = models.ImageField(upload_to='patient_pics/', blank=True, null=True)
    patient_info = models.TextField(blank=True, null=True)
    patient_medications = models.TextField(blank=True, null=True)
    patient_surgeries = models.TextField(blank=True, null=True)
    patient_social_history = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.user.name} {self.user.surname} - {self.department.name}"

## Normalization for future proofing