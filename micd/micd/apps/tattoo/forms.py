from django import forms
from micd.apps.tattoo.models import Tattoo, Comentario


class TattooForm(forms.ModelForm):
    class Meta:
        model = Tattoo
        fields = [
            'nombre',
            'descripcion',
            'precio',
            'categoria',
            'imagen',
        ]
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
            'precio': 'Precio',
            'categoria': 'Categoria',
            'imagen': 'Imagen',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = [
            'tattoo',
            'isuario',
            'comentario',
        ]
        labels = {
            'tattoo': 'Tattoo',
            'isuario': 'Ingresa un nombre',
            'comentario': 'Escribe un comentario',
        }
        widgets = {
            'isuario': forms.TextInput(attrs={'class': 'form-control'}),
            'comentario': forms.TextInput(attrs={'class': 'form-control'}),
        }
