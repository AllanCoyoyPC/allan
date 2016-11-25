from django.shortcuts import render, get_object_or_404, redirect, render_to_response
# Create your views here.
from django.contrib import messages
from django.template import RequestContext
from django.core.urlresolvers import reverse
from .forms import TiendaForm, ProductoForm, InventarioForm,TiendaForm2
from tiendas.models import Tienda, Inventario, Producto
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

id_tienda = 0

@login_required
def tienda_lista(request):
    tiendas = Tienda.objects.all
    return render(request, 'tienda/tienda_lista.html', {'tiendas':tiendas})

@login_required
def tienda_detalle(request, pk):
    tiendas = get_object_or_404(Tienda, pk=pk)
    return render(request, 'tienda/tienda_detalle.html', {'tiendas': tiendas})

@login_required
def tienda_nueva(request):
    if request.method == "POST":
        formulario = TiendaForm(request.POST,request.FILES)
        if formulario.is_valid():
            tienda = formulario.save(commit=False)
            tienda = Tienda(nombre=formulario.cleaned_data['nombre'],
            direccion=formulario.cleaned_data['direccion'],
            telefono=formulario.cleaned_data['telefono'],
            foto=request.FILES)
            formulario.save()
    else:
        formulario = TiendaForm()
    return render(request, 'tienda/tienda_nueva.html', {'formulario': formulario})

@login_required
def tienda_editar(request,pk):
    tienda = get_object_or_404(Tienda, pk=pk)
    if request.method == "POST":
        formulario = TiendaForm(request.POST,request.FILES, instance = tienda)
        if formulario.is_valid():
            tienda=formulario.save(commit=False)
            tienda.save()
        return redirect('tiendas.views.tienda_detalle', pk=tienda.pk)

    else:
        formulario = TiendaForm(instance=tienda)
    return render(request, 'tienda/tienda_editar.html', {'formulario': formulario})

def tienda_eliminar(request, pk):
    tienda = get_object_or_404(Tienda, pk=pk)
    tienda.delete()
    return redirect('tiendas.views.tienda_lista')

@login_required
def tienda_nueva2(request):
    if request.method == "POST":
        formulario = TiendaForm2(request.POST,request.FILES)
        if formulario.is_valid():
            tienda = formulario.save(commit=False)
            tienda = Tienda.objects.create(nombre=formulario.cleaned_data['nombre'],
            direccion=formulario.cleaned_data['direccion'],
            telefono=formulario.cleaned_data['telefono'],
            foto=request.FILES)
            for producto_id in request.POST.getlist('productos'):
               tienda.save()
               messages.add_message(request, messages.SUCCESS, 'Tienda Creada Exitosamente')
    else:
        formulario = TiendaForm2()
    return render(request, 'tienda/tienda_nueva.html', {'formulario': formulario})

@login_required
def producto_lista(request):
    productos = Producto.objects.all
    return render(request, 'producto/producto_lista.html', {'productos':productos})

@login_required
def producto_detalle(request, pk):
    productos = get_object_or_404(Producto, pk=pk)
    return render(request, 'producto/producto_detalle.html', {'productos': productos})

@login_required
def producto_nuevo(request):
    if request.method == "POST":
        formulario = ProductoForm(request.POST,request.FILES)
        if formulario.is_valid():
            producto = formulario.save(commit=False)
            producto = Producto(nombre=formulario.cleaned_data['nombre'],
            foto=request.FILES,
            precio=formulario.cleaned_data['precio'],
            )
            formulario.save()
        return redirect('producto_lista')
    else:
        formulario = ProductoForm()
    return render(request, 'producto/producto_nueva.html', {'formulario': formulario})

@login_required
def producto_editar(request,pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        formulario = ProductoForm(request.POST,request.FILES, instance = producto)
        if formulario.is_valid():
            producto=formulario.save(commit=False)
            producto.save()
        return redirect('tiendas.views.producto_detalle', pk=producto.pk)

    else:
        formulario = ProductoForm(instance=producto)
    return render(request, 'producto/producto_editar.html', {'formulario': formulario})

@login_required
def producto_eliminar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('tiendas.views.producto_lista')

@login_required
def inventario_nuevo(request):
    if request.method == "POST":
        formulario = InventarioForm(request.POST)
        if formulario.is_valid():
            for tienda_id in request.POST.getlist('tienda'):
                idt = tienda_id
            for producto_id in request.POST.getlist('producto'):
               inventario = Inventario(producto_id=producto_id, tienda_id = tienda_id)
               inventario.save()
               messages.add_message(request, messages.SUCCESS, 'Inventario Asignado Exitosamente')
    else:
        formulario = InventarioForm()
    return render(request, 'tienda/inventario_nuevo.html', {'formulario': formulario})
