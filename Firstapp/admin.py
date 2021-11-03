from django.contrib import admin


from .models import *


models = [CartProduct, Cart, Customer, Category,Product]
for model in models:
    admin.site.register(model)