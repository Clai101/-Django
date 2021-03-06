from django.views.generic import View
from .models import Cart, Customer

class CartMixin(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            customer = Customer.objects.filter(user=request.user).first()
            if not customer:
                customer = Customer.objects.create(user=request.user)
            self.customer = customer
            cart = Cart.objects.filter(owner=customer, in_order=False).first()
            if not cart:
                cart = Cart.objects.create(owner=customer)
        else:
            cart = Cart.objects.filter(for_anonym_user=True).first()
            if not cart:     
                cart = Cart.objects.create(for_anonym_user=True)
        self.cart = cart
        if self.cart.finl_price == None:
            self.price = 0
            self.cart.finl_price = 0
        else:
            self.price = self.cart.finl_price
        return super().dispatch(request, *args, **kwargs)


