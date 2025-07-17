from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Auth status path
    path('auth-status/', views.auth_status, name='auth_status'),

    # Registration paths
        # Login path
    path('login', LoginView.as_view(template_name="core/registration/login.html"), name='login'),
        # Signup path
    path('signup', views.signup, name='signup'),
        # Logout path
    path('logout', LogoutView.as_view(next_page="login"), name='logout'),
    
    # Explore and discover paths
    path('discover', views.discover, name='discover'),
    path('explore', views.explore, name='explore'),

    #Dashboard paths
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard-patient', views.dashboard_patient, name='dashboard_patient'),
    path('dashboard-staff', views.dashboard_staff, name='dashboard_staff'),
]