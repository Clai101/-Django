from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from Firstapp import main_list






urlpatterns = [
    path('shop/', main_list, name='main'),
   ]
   