from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from .views import MainListView, ProductDetailView, DeleteFromCartView, AddToCartView, CartView






urlpatterns = [
    path('', MainListView.as_view(), name='main'),
    path('products/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add_to_cart/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:slug>/', ProductDetailView.as_view(), name='remove_from_cart'),

   ]
   