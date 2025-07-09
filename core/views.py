from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'core/registration/login.html')
def signup(request):
    return render(request, 'core/registration/signup.html')

def discover(request):
    return render(request, 'core/discover.html')
def explore(request):
    return render(request, 'core/explore.html')