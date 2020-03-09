from django import forms
from inventory.models import *
from inventory.forms import *

class Category(forms.ModelForm):
    category = forms.CharField(max_length=50)

class Item(forms.ModelForm):
    name     = forms.CharField(required=True, max_length=50, label="Name: ")
    category = forms.CharField(required=True, max_length=50, label="Category: ")
    serial   = forms.CharField(required=True, max_length=15, label="Serial Number: ")
    caliber  = forms.CharField(required=True, max_length=8,  label="Caliber: ")
    quantity = forms.IntegerField(required=False, label="Quantity: ")
