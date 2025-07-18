from django.shortcuts import render

# Create your views here.

from .models import Doctor, Department

def doctor_list(request):
    department_name = request.GET.get('department')
    if department_name and department_name != 'all':
        doctors = Doctor.objects.filter(department__name__iexact=department_name)
    else:
        doctors = Doctor.objects.all()
    departments = Department.objects.all()
    return render(request, "hospital/doctor_cards.html", {
        "doctors": doctors,
        "departments": departments,
        "selected_department": department_name or "all"
    })