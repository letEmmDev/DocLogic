from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import PatientReportViewSet

router = DefaultRouter()
router.register(r'api/patients-reports', PatientReportViewSet)

urlpatterns = [
    path('patients/', views.patient_list, name='patient_list'),
    path('edit_patient/<int:patient_id>/', views.edit_patient, name='edit_patient'),
    
    ## Partials paths
    path('report_patient/<int:patient_id>/info_form/', views.patient_info_form, name='patient_info_form'),
    path('report_patient/<int:patient_id>/medications_form/', views.patient_medications_form, name='patient_medications_form'),
    path('report_patient/<int:patient_id>/surgeries_form/', views.patient_surgeries_form, name='patient_surgeries_form'),
    path('report_patient/<int:patient_id>/social_history_form/', views.patient_social_history_form, name='patient_social_history_form'),
] + router.urls