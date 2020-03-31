from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView
from micd.apps.tattoo.models import Tattoo
from micd.apps.tattoo.forms import TattooForm

# Create your views here.

class TattooList(ListView):
    model = Tattoo
    template_name = 'tattoo_list.html'

class ProductCreate(CreateView):
    model = Tattoo
    form_class = TattooForm
    template_name = 'tattoo_form.html'
    success_url = reverse_lazy('list_tattoo')