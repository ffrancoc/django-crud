from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(blank=None, null=None, max_length=100)
    cantidad = models.IntegerField(blank=None, null=None)
    precio = models.DecimalField(blank=None, null=None, max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return f"nombre= {self.nombre}, cantidad= {self.cantidad}, precio= {self.precio}"