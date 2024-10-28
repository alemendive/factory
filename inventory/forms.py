from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):  # Establecer clases CSS para los campos
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control', 'min': '0', 'step': '0.01'})  # Permite decimales
        self.fields['min_stock'].widget.attrs.update({'class': 'textinput form-control', 'min': '0', 'step': '0.01'})  # Permite decimales  # Estilo para min_stock

    class Meta:
        model = Stock
        fields = ['name', 'quantity', 'min_stock']  # Agregar 'min_stock' a los campos