from django.contrib import admin
from tiendas.models import Producto, ProductoAdmin, Tienda, TiendaAdmin, Inventario

#Registramos nuestras clases principales.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Tienda, TiendaAdmin)
admin.site.register(Inventario)
