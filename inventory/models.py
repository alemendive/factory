from django.db import models

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    category = models.CharField(
        max_length=50,
        choices=[
            ('Limpiadores varios', 'Limpiadores varios'),
            ('Productos para piscinas', 'Productos para piscinas'),
            ('Higiene personal', 'Higiene personal'),
            ('Desodorantes de piso', 'Desodorantes de piso'),
            ('Ceras de pisos', 'Ceras de pisos'),
            ('Perfumes de telas', 'Perfumes de telas'),
            ('Lavado de ropas', 'Lavado de ropas'),
            ('Envases y afines', 'Envases y afines'),
            ('Difusores ambientales', 'Difusores ambientales'),
            ('Productos para autos', 'Productos para autos'),
            ('Escencias de perfumes y desodorantes', 'Escencias de perfumes y desodorantes')
        ]
    )
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    min_stock = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_composite = models.BooleanField(default=False)
    parent_material = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='submaterials',
        help_text="Define si este material es un submaterial de otro"
    )
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def update_quantity_on_sale(self, quantity_sold):
        if quantity_sold > self.quantity:
            raise ValueError("Cantidad insuficiente en el inventario")
        self.quantity -= quantity_sold
        self.save()
        self.check_min_stock()

    def check_min_stock(self):
        if self.quantity <= self.min_stock:
            print(f"Alerta: El stock de {self.name} ha llegado al mínimo. ¡Es momento de reabastecer!")
