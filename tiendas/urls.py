from django.conf.urls import url
from django.conf import settings
from . import views
#para llamar a nuestra página para insertar tenemos que invocar la dirección /pelicula/nueva

# se puede crear un hipervinculo para llamarla, en este ejemplo hay que invocar manualmente la dirección.

urlpatterns = [
    url(r'^$', views.tienda_lista),
    url(r'^tienda/$', views.tienda_nueva2, name='tienda_nueva2'),
    url(r'^tienda/nueva/$', views.tienda_nueva, name='tienda_nueva'),
    url(r'^tienda/(?P<pk>[0-9]+)/$', views.tienda_detalle, name='tienda_detalle'),
    url(r'^tienda/(?P<pk>[0-9]+)/editar/$', views.tienda_editar, name='tienda_editar'),
    url(r'^tienda/(?P<pk>\d+)/eliminar/$', views.tienda_eliminar, name='tienda_eliminar'),
    url(r'^productos/$', views.producto_lista, name='producto_lista'),
    url(r'^inventario$', views.inventario_nuevo, name='inventario_nuevo'),
    url(r'^producto/nuevo/$', views.producto_nuevo, name='producto_nuevo'),
    url(r'^producto/(?P<pk>[0-9]+)/$', views.producto_detalle, name='producto_detalle'),
    url(r'^producto/(?P<pk>[0-9]+)/editar/$', views.producto_editar, name='producto_editar'),
    url(r'^producto/(?P<pk>\d+)/eliminar/$', views.producto_eliminar, name='producto_eliminar'),
    ]
