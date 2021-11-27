from django import forms
from .models import Order, USER

class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data'].label = 'Дата доставки'
    data = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Order
        fields = ('adress',
                  'first_name',
                  'last_name',
                  'phone',
                  'data',)

