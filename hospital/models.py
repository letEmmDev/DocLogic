from django.db import models

# Create your models here.

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    technologies = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Specialization(models.Model):
    specialization_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='doctors')
    specialization = models.ForeignKey('Specialization', on_delete=models.CASCADE, related_name='doctors')
    profile_picture = models.ImageField(upload_to='doctor_pics/', blank=True, null=True)
    user = models.ForeignKey('core.CustomUser', on_delete=models.CASCADE, related_name='doctor_profile')

    def __str__(self):
        return f"{self.user.name} {self.user.surname} - {self.specialization}"

class Hospital(models.Model):
    hospital_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=100)
    active_staff = models.IntegerField(default=0)
    patient_capacity = models.IntegerField(default=0)
    services = models.ManyToManyField(Service, related_name='hospitals')
    
    def __str__(self):
        return self.name
