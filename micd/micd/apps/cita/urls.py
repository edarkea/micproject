from django.urls import path
from micd.apps.cita.views import cita_form

urlpatterns = [
    path('add', cita_form, name='create_cita'),
]