from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin URL configuration
    path('admin/', admin.site.urls),
    # Include other app URLs
        ## Core app URLs
    path('', include('core.urls')),
        ## Hospital app URLs
    path('hospital/', include('hospital.urls')),
        ## Patient app URLs
    path('patients_management/', include('patient_management.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)