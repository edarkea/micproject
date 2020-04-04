from django.shortcuts import render
from django.http import HttpResponse
from micd.apps.tattoo.models import Tattoo, Comentario
# Create your views here.


def index(request):
    tattoos = Tattoo.objects.all().order_by('id')
    data = dict()
    for tattoo in tattoos:
        comentarios = Comentario.objects.filter(tattoo=tattoo)
        data[tattoo] = []
        for comentario in comentarios:
            data[tattoo].append(comentario)

    return render(request, 'index.html', {"object_list": data})
