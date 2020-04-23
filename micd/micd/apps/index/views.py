from django.shortcuts import render
from django.http import HttpResponse
from micd.apps.tattoo.models import Tattoo, Comentario
from django.db.models import Q

import json

# Create your views here.


def index(request):
    queryset = request.GET.get("buscar")
    tattoos = Tattoo.objects.all().order_by('id')
    if queryset:
        tattoos = Tattoo.objects.filter(
            Q(nombre=queryset) |
            Q(descripcion=queryset)
        ).distinct()

    data = dict()
    for tattoo in tattoos:
        comentarios = Comentario.objects.filter(tattoo=tattoo)
        data[tattoo] = []
        for comentario in comentarios:
            data[tattoo].append(comentario)

    return render(request, 'index.html', {"object_list": data})
