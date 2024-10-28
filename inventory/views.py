from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    CreateView, 
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Stock
from .forms import StockForm
from django_filters.views import FilterView
from .filters import StockFilter
from django.db.models import F  # Importar F aquí

class StockListView(FilterView):
    filterset_class = StockFilter
    queryset = Stock.objects.filter(is_deleted=False).order_by('quantity')  # Ordenar por cantidad de menor a mayor
    template_name = 'inventory.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["low_stock_items"] = Stock.objects.filter(quantity__lte=F('min_stock'))
        return context

class StockCreateView(SuccessMessageMixin, CreateView):
    model = Stock
    form_class = StockForm
    template_name = "edit_stock.html"
    success_url = '/inventory'
    success_message = "El stock ha sido creado con éxito"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nuevo material'
        context["savebtn"] = 'Agregar'
        return context       

class StockUpdateView(SuccessMessageMixin, UpdateView):
    model = Stock
    form_class = StockForm
    template_name = "edit_stock.html"
    success_url = '/inventory'
    success_message = "El material del Stock ha sido actualizado"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Editar Stock'  # Corregido para español
        context["savebtn"] = 'Actualizar Stock'  # Corregido para español
        context["delbtn"] = 'Eliminar Stock'  # Corregido para español
        return context

class StockDeleteView(View):
    template_name = "delete_stock.html"
    success_message = "El material del Stock ha sido eliminado"
    
    def get(self, request, pk):
        stock = get_object_or_404(Stock, pk=pk)
        return render(request, self.template_name, {'object': stock})

    def post(self, request, pk):  
        stock = get_object_or_404(Stock, pk=pk)
        stock.is_deleted = True
        stock.save()                                               
        messages.success(request, self.success_message)
        return redirect('inventory')
