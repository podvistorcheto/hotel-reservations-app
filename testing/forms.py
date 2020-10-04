from django import forms
from .models import Product


class ProductForm(forms.Form):
    first_name = forms.CharField(max_length=256)
    last_name = forms.CharField(max_length=256)
    date_started = forms.DateField()
    date_due = forms.DateField()
