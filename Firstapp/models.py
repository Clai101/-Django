from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse

USER = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.title

class Product(models.Model):
    
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255,verbose_name='Название продукта')
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=9,decimal_places=2, verbose_name = 'Цена продукта')
    image = models.ImageField(verbose_name = 'Картинка продукта')
    description = models.TextField(verbose_name = 'Описание продукта', null=True)
    def __str__(self):
        return self.title
    
    
class CartProduct(models.Model):
    user = models.ForeignKey('Customer',on_delete=models.CASCADE,verbose_name='Покупатель')
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE,verbose_name='Корзина',related_name = 'related_product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField(default=1)
    final_price =  models.DecimalField(max_digits=9,decimal_places=2, null=True, verbose_name = 'Финальная цена продукта')
    def __str__(self):
        return self.content_object.title


class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Владлец',on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    total_products = models.PositiveIntegerField(default=0)
    finl_price =  models.DecimalField(max_digits=9,decimal_places=2, null=True, verbose_name = 'Финальная цена продуктов')
    products = models.ManyToManyField(CartProduct, verbose_name='Продукты', related_name = 'related_cart')
    in_order = models.BooleanField(default=False)
    for_anonym_user = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(USER, verbose_name='Пользователь',on_delete=models.CASCADE)
    phone = models.CharField(max_length=25,null=True,blank=True, verbose_name='Номер телефона' )
    adress = models.CharField(max_length=255,null=True,blank=True, verbose_name='Адрес' )
    def __str__(self):
        return f'Покупатель {self.user.first_name,self.user.last_name} '