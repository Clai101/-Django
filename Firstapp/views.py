from django.shortcuts import render
from django.views.generic import DetailView
from .models import SmartPhone, WoshMachin, LatestProductManager
from django.views import View


class MainListView(View):
    def get(self, request, *args, **kwargs):
        last_product = LatestProductManager.objects.show_product('smartphone','woshmachin')

        context = {'last_product':last_product}
        return render(request, 'Firstapp/index.html', context)



class ProductDetailView(DetailView):
    CT_MODELS = {
        'smartphone': SmartPhone,
        'woshmachin' : WoshMachin,
        }
    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODELS[kwargs['ct_model']]
        self.queryset = self.model.objects.all()
        return super().dispatch(request, *args, **kwargs)
    context_object_name = 'product'
    template_name = 'Firstapp/product.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ct_model'] = self.model._meta.model_name
        return context

