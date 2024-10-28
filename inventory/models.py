# inventory/models.py
from django.db import models

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Permite decimales
    min_stock = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Permite decimales
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def update_quantity_on_sale(self, quantity_sold):
        if quantity_sold > self.quantity:
            raise ValueError("Cantidad insuficiente en el inventario")
        self.quantity -= quantity_sold
        self.save()
        self.check_min_stock()  # Verificar stock mínimo después de cada actualización

    def check_min_stock(self):
        if self.quantity <= self.min_stock:
            # Alerta para reabastecer cuando el stock está por debajo del mínimo
            # Puedes manejar esta alerta con un mensaje o un envío de notificación
            print(f"Alerta: El stock de {self.name} ha llegado al mínimo. ¡Es momento de reabastecer!")
