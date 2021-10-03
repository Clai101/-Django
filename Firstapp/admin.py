from django.contrib import admin
from django import forms
# Register your models here.

from .models import *

class SmartPhoneAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self,db_field, request, **kwargs):
        if db_field.name =='category':
            return forms.ModelChoiceField(Category.objects.filter(slug='smartphone'))
        return super().formfield_for_foreignkey(db_field,request, **kwargs)

models = [SmartPhone, WoshMachin, CartProduct, Cart, Customer, Category]

for model in models:
    if model==SmartPhone:
        admin.site.register(model,SmartPhoneAdmin)
    else:

        admin.site.register(model)
        
