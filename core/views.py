from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
## Import the customed form so it can be used in the signup view
from .decorators import patient_required, staff_required
from hospital.models import Department, Doctor, Hospital
from patient_management.models import Patient

# Create your views here.
def home(request):
    return render(request, 'home.html')

## Registration views
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, initial={'role': 'user'})
        if form.is_valid():
            print("Form is valid!")  # Debug
            user = form.save()
            print("User saved:", user)  # Debug
            login(request, user)
            return redirect('dashboard')
        else:
            print("Form errors:", form.errors)  # Debug
    else:
        form = CustomUserCreationForm(initial={'role': 'user'})    
    return render(request, 'core/registration/signup.html', {'form': form})

def auth_status(request):
    return render(request, 'core/auth_status.html')

## Landing page path 
def discover(request):
    return render(request, 'core/discover.html')
def explore(request):
    return render(request, 'core/explore.html')

## Access based dashboard paths
@patient_required
def dashboard_patient(request):
    departments = Department.objects.all()
    doctors = Doctor.objects.all()  # Or filter as needed for initial load
    hospital = Hospital.objects.first()
    return render(request, 'core/dashboard/dashboard_patient.html', {
        'departments': departments,
        'doctors': doctors,
        'hospital': hospital,
    })

@staff_required
def dashboard_staff(request):
    patients = Patient.objects.all()
    departments = Department.objects.all()
    return render(request, 'core/dashboard/dashboard_staff.html', {
        'patients': patients,
        'departments': departments,
    })

def admin_validation(request):
    return render(request, 'core/dashboard/admin_validation.html')
## Dashboard views
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.role == 'staff':
        return redirect('dashboard_staff')
    if request.user.role == 'patient':
        return redirect('dashboard_patient')
    else:
        return redirect('admin_validation')