from django import forms
from .models import Product

class ProductAdd(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_id','product_name','product_price','product_quantity',)
