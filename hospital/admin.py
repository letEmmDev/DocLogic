from django.contrib import admin

# Register your models here.

from .models import Department, Service, Doctor, Hospital

admin.site.register(Department)
admin.site.register(Service)
admin.site.register(Doctor)
admin.site.register(Hospital)