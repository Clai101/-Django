from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from .views import MainListView, ProductDetailView






urlpatterns = [
    path('', MainListView.as_view(), name='main'),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),

   ]
   