from django.db import models

def  refresh_cart(cart):
    cart_data = cart.products.aggregate(models.Sum('final_price'),models.Count('id'))
    cart.final_price = cart_data.get('final_price__sum')
    cart.total_products =  cart_data['id__count']
    cart.save()