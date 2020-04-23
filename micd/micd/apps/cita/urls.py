from django.urls import path
from micd.apps.cita.forms import ContactForm

urlpatterns = [
    path('add', ContactForm, name='create_cita'),
]