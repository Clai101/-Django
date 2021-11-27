from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Product, Customer, CartProduct
from django.views import View
from .mixins import CartMixin
from .utils import refresh_cart
from .forms import OrderForm

class MainListView(View):
    def get(self, request, *args, **kwargs):
        last_product = Product.objects.all()
        context = {'last_product':last_product, }
        return render(request, 'Firstapp/index.html', context)

class CartView(CartMixin,View):
    def get(self, request, *args, **kwargs):
       
        context = {'cart':self.cart, }
        return render(request, 'Firstapp/cart.html', context)

class DeleteFromCartView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        print("________________")
        product_slug = kwargs.get('slug')
        print("________________")
        product = Product.objects.get(slug = product_slug)
        print("________________")
        cart_product = CartProduct.objects.get(
                                                product=product,
                                                user=self.cart.owner,
                                                cart=self.cart,
                                                )
        print("________________")
        self.cart.products.remove(cart_product)
        print("________________")
        refresh_cart(self.cart)
        return redirect('/cart/')

class AddToCartView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        product_slug = kwargs.get('slug')
        product = Product.objects.get(slug = product_slug)
        cart_product, created = CartProduct.objects.get_or_create(
                                                                  product = product,
                                                                  user = self.cart.owner,
                                                                  cart = self.cart,
                                                                 
                                                                  )
        if created:
            self.cart.products.add(cart_product)
        refresh_cart(self.cart)
        return redirect('/cart/')
    
class ChangeQuantityInCartView(CartMixin, View):
    def post(self, request, *args, **kwargs):
      
        product_slug = kwargs.get('slug')
        product = Product.objects.get(slug = product_slug)
        cart_product = CartProduct.objects.get(
                                                product = product,
                                                user = self.cart.owner,
                                                cart = self.cart,
                                               
                                                )
        quantity = int(request.POST.get('quantity'))
        print(quantity)
        cart_product.quantity = quantity
        cart_product.final_price = quantity*product.price
        cart_product.save()
        refresh_cart(self.cart)
        return redirect('/cart/')



class ProductDetailView(DetailView):
    context_object_name = 'product'
    template_name = 'Firstapp/product.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class OrderView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        context = {
            'cart':self.cart,
            'form':form 
            }
        return render(request, 'Firstapp/order.html', context)
    
class MakeOrderView(CartMixin, View):
    def post(self, request, *args, **kwargs):
         form = OrderForm(request.POST)
         if form.is_valid():
             new_order = form.save(commit=False)
             new_order.customer = self.customer
             new_order.first_name = form.cleaned_data['first_name']
             new_order.save()
             self.cart.in_order = True
             self.cart.save()
             new_order.cart = self.cart
             new_cart.save()
             self.customer.orders.add(new_order)
             return redirect('/')
         return redirect('/order/')

