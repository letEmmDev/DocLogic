from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
## Import the customed form so it can be used in the signup view

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
            return redirect('home')
        else:
            print("Form errors:", form.errors)  # Debug
    else:
        form = CustomUserCreationForm(initial={'role': 'user'})    
    return render(request, 'core/registration/signup.html', {'form': form})

## Landing page path 
def discover(request):
    return render(request, 'core/discover.html')
def explore(request):
    return render(request, 'core/explore.html')