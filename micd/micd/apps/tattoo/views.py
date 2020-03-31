from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView
from micd.apps.tattoo.models import Tattoo

# Create your views here.

class TattooList(ListView):
    model = Tattoo
    template_name = 'tattoo_list.html'