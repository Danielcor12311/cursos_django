from django import forms
from .models import Cursos

class CursosForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ['nombre','descripcion', 'nivel', 'precio', 'fecha_inicio', 'imagen']