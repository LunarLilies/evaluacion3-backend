from django.db import models

# Create your models here.

class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre_prod = models.CharField(max_length=100, blank=False)
    precio      = models.IntegerField(blank=False, null=False)
    descripcion = models.CharField(max_length=500)