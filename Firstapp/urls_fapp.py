from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from .views import MainListView, ProductDetailView, DeleteFromCartView, AddToCartView, CartView, ChangeQuantityInCartView, OrderView, MakeOrderView






urlpatterns = [
    path('', MainListView.as_view(), name='main'),
    path('products/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add_to_cart/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:slug>/', DeleteFromCartView.as_view(), name='remove_from_cart'),
    path('change_quantity/<str:slug>/', ChangeQuantityInCartView.as_view(), name='change_quantity'),
    path('order/', OrderView.as_view(), name='order'),
    path('make_order/', MakeOrderView.as_view(), name='make_order'),

   ]
   