from django.urls import path
from . import views

# Your codes come below here

urlpatterns = [
    path('', views.home, name='home'),
    path('password/', views.password, name='password'),
    path('about/', views.about, name='about'),
]