from django import forms
from .models import Marca, Modelo, Version, Vehiculo, Cliente, Vendedor, Pais, Ventas

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

# Repite para los demás modelos
