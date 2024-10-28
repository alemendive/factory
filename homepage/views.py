from django.shortcuts import render
from django.views.generic import View, TemplateView
from inventory.models import Stock
from transactions.models import SaleBill, PurchaseBill


class HomeView(View):
    template_name = "home.html"
    
    def get(self, request):        
        labels = []
        data = []
        min_stock = []

        stockqueryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')
        for item in stockqueryset:
            labels.append(item.name)
            data.append(item.quantity)
            min_stock.append(item.min_stock)  # Agrega el mínimo de seguridad

        sales = SaleBill.objects.order_by('-time')[:3]
        purchases = PurchaseBill.objects.order_by('-time')[:3]
        
        context = {
            'labels': labels,
            'data': data,
            'min_stock': min_stock,  # Agrega esta lista al contexto
            'sales': sales,
            'purchases': purchases,
        }
        return render(request, self.template_name, context)


class AboutView(TemplateView):
    template_name = "about.html"