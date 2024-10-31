from django.contrib import admin
from .models import Stock

class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'min_stock', 'category', 'is_deleted')
    list_filter = ('is_deleted','category')
    search_fields = ('name', 'quantity', 'min_stock', 'category')
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_deleted=False)  # Solo muestra materiales no eliminados




admin.site.register(Stock, StockAdmin)