# forms.py
from django import forms
from .models import Stock


class StockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control', 'min': '0', 'step': '0.01'})
        self.fields['min_stock'].widget.attrs.update({'class': 'textinput form-control', 'min': '0', 'step': '0.01'})
        self.fields['category'].widget.attrs.update({'class': 'form-select'})
        self.fields['is_composite'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['parent_material'].widget.attrs.update({'class': 'form-select'})

    class Meta:
        model = Stock
        fields = ['name', 'category', 'quantity', 'min_stock', 'is_composite', 'parent_material']
