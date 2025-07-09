from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Registration paths
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    
    # Explore and discover paths
    path('discover', views.discover, name='discover'),
    path('explore', views.explore, name='explore'),
]