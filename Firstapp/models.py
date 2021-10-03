from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse

USER = get_user_model()


def make_product_url(object,viewname):
    ct_model = object.__class__._meta.model_name
    
    return reverse(viewname, kwargs={' ct_model':ct_model, 'slug':object.slug})


class LatestProduct:
    def show_product(*args,**kwargs):
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for cat_model in ct_models:
            model_products = cat_model.model_class().objects.all().order_by('-id')[:5]
            products.extend(model_products)
        return products

    

class LatestProductManager:
    objects = LatestProduct()

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.title

class Product(models.Model):
    class Meta:
        abstract = True
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255,verbose_name='Название продукта')
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=9,decimal_places=2, verbose_name = 'Цена продукта')
    image = models.ImageField(verbose_name = 'Картинка продукта')
    description = models.TextField(verbose_name = 'Описание продукта', null=True)
    def __str__(self):
        return self.title

class SmartPhone(Product):
    diagonal = models.CharField(max_length=255, verbose_name='Диагональ')
    charge_capacity = models.CharField(max_length=255, verbose_name='Емкость батареи')
    data_capacity = models.CharField(max_length=255, verbose_name='Память')
    ram = models.CharField(max_length=255, verbose_name='Оперативная память')
    def get_absolute_url(self):
        return make_product_url(self, 'product')
    
class WoshMachin(Product):
    qantity_turnover = models.CharField(max_length=255, verbose_name='Количество оборотов')
    capacity = models.CharField(max_length=255, verbose_name='Емкость')
    qantity_of_modes = models.CharField(max_length=255, verbose_name='Количество режимов')
    def get_absolute_url(self):
        return make_product_url(self, 'product_detail')

class CartProduct(models.Model):
    user = models.ForeignKey('Customer',on_delete=models.CASCADE,verbose_name='Покупатель')
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE,verbose_name='Корзина',related_name = 'related_product')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) 
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)
    finl_price =  models.DecimalField(max_digits=9,decimal_places=2, verbose_name = 'Финальная цена продукта')
    def __str__(self):
        return self.content_object.title


class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Владлец',on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    total_products = models.PositiveIntegerField(default=0)
    finl_price =  models.DecimalField(max_digits=9,decimal_places=2, verbose_name = 'Финальная цена продуктов')
    products = models.ManyToManyField(CartProduct, verbose_name='Продукты', related_name = 'related_cart')

    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(USER, verbose_name='Пользователь',on_delete=models.CASCADE)
    phone = models.CharField(max_length=25,null=True,blank=True, verbose_name='Номер телефона' )
    adress = models.CharField(max_length=255,null=True,blank=True, verbose_name='Адрес' )
    def __str__(self):
        return f'Покупатель {self.user.first_name,self.user.last_name} '