from django.db import models
from django.contrib import admin

# Create your models here.

class Producto(models.Model):
    nombre  =   models.CharField(max_length=30)
    foto = models.ImageField(upload_to='tiendas/imagen/')
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Tienda(models.Model):
    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    telefono = models.CharField(max_length=15)
    foto = models.ImageField(upload_to='tiendas/imagen/',blank=True, null=True)
    productos = models.ManyToManyField(Producto, through='Inventario')
    def __str__(self):
        return self.nombre

class Inventario (models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)

class InventarioInLine(admin.TabularInline):
    model = Inventario
    extra = 1

class ProductoAdmin(admin.ModelAdmin):
    inlines = (InventarioInLine,)

class TiendaAdmin (admin.ModelAdmin):
    inlines = (InventarioInLine,)
