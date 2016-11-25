from django import forms
from .models import Tienda, Producto, Inventario


class TiendaForm(forms.ModelForm):
    class Meta:
        model = Tienda
        fields = ('nombre', 'direccion','telefono','foto')

class TiendaForm2(forms.ModelForm):
    class Meta:
        model = Tienda
        fields = ('nombre', 'direccion','telefono','productos')

def __init__ (self, *args, **kwargs):
        super(TiendaForm, self).__init__(*args, **kwargs)
        self.fields["productos"].widget = forms.CheckboxSelectMultiple()
        self.fields["productos"].help_text = "Ingrese los Productos que pertenecerán a la tienda"
        self.fields["productos"].queryset = Producto.objects.all()

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'foto','precio')

class InventarioForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Inventario
        fields = ('tienda', 'producto')

def __init__ (self, *args, **kwargs):
        super(TiendaForm, self).__init__(*args, **kwargs)
        self.fields["producto"].widget = forms.CheckboxSelectMultiple()
        self.fields["producto"].help_text = "Ingrese los Productos que pertenecerán a la tienda"
        self.fields["producto"].queryset = Producto.objects.all()

def __init__ (self, *args, **kwargs):
        super(TiendaForm, self).__init__(*args, **kwargs)
        self.fields["tienda"].widget = forms.CheckboxSelectMultiple()
        self.fields["tienda"].help_text = "Ingrese la Tienda a la que pertenecerán los productos"
        self.fields["tienda"].queryset = Tienda.objects.all()
