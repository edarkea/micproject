from django import forms
from micd.apps.tattoo.models import Tattoo

class TattooForm(forms.ModelForm):
    class Meta:
        model = Tattoo
        fields = [
            'nombre',
            'descripcion',
            'precio',
            'imagen',
        ]
        labels={
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
            'precio': 'Precio',
            'imagen': "Imagen",
        }
        widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.NumberInput(attrs={'class':'form-control'}),
        }