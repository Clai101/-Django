"""
Definition of urls for ПрактикаDjango.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView







urlpatterns = [
    path('admin/', admin),
    path('', include("Fristapp.urls_fapp"))
    
   ]
   