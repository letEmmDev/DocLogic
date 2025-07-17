from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
## Import the customed form so it can be used in the signup view
from .decorators import patient_required, staff_required

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
    return render(request, 'core/dashboard/dashboard_patient.html')
@staff_required
def dashboard_staff(request):
    return render(request, 'core/dashboard/dashboard_staff.html')

## Dashboard views
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.role == 'patient':
        return redirect('dashboard_patient')
    else:
        return redirect('dashboard_staff')