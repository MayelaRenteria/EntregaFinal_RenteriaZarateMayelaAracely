from django import forms
from .models import Corte, Peinado, Estilista

class CorteForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea)
    precio = forms.DecimalField(max_digits=8, decimal_places=2)
    duracion_minutos = forms.IntegerField()
    

class PeinadoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea)
    precio = forms.DecimalField(max_digits=8, decimal_places=2)
    duracion_minutos = forms.IntegerField()
    
class EstilistaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=15)
    email = forms.EmailField()
    especialidad = forms.CharField(max_length=100)
    experiencia_anios = forms.IntegerField()

    
    