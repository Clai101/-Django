from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Product, Customer, CartProduct
from django.views import View
from .mixins import CartMixin


class MainListView(View):
    def get(self, request, *args, **kwargs):
        last_product = Product.objects.all()
        
        context = {'last_product':last_product, }
        return render(request, 'Firstapp/index.html', context)

class CartView(CartMixin,View):
    def get(self, request, *args, **kwargs):
        context = {'cart':self.cart}
        return render(request, 'Firstapp/cart.html', context)

class DeleteFromCartView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        product_slug = kwargs.get('slug')
        product = Product.objects.get(slug = product_slug)
        cart_product = CartProduct.objects.get(product=product, user=self.cart.owner, cart=self.cart,final_price=0)
        self.cart.products.remove(cart_product)
        cart_product.delete()
        return redirect('/cart/')

class AddToCartView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        product_slug = kwargs.get('slug')
        product = Product.objects.get(slug = product_slug)
        cart_product, created = CartProduct.objects.get_or_create(
                                                                  product = product,
                                                                  user = self.cart.owner,
                                                                  cart = self.cart,
                                                                  final_price = 0
                                                                  )
        if created:
            self.cart.products.add(cart_product) 
     
        return redirect('/cart/')



class ProductDetailView(DetailView):
    
    context_object_name = 'product'
    template_name = 'Firstapp/product.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

