from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('contact/', views.contact_form, name='contact_form'),
]