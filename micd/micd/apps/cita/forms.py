from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre",
    )

    email = forms.EmailField(
        label="Correo",
    )

    message = forms.CharField(
        label="Email",
        widget=forms.Textarea,
    )