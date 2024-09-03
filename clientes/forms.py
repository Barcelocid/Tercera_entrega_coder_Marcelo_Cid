from django import forms
from .models import cliente, pais, comida

class PaisForm(forms.ModelForm):
    class Meta:
        model = pais
        fields = ['pais','ciudad']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['nombre', 'apellido', 'rut']

class ComidaForm(forms.ModelForm):
    class Meta:
        model = comida
        fields = ['fondo', 'bebida', 'postre']
