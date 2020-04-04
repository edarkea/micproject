from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView
from micd.apps.tattoo.models import Tattoo, Categoria, Comentario
from micd.apps.tattoo.forms import TattooForm, CommentForm

# Create your views here.


class TattooList(ListView):
    model = Tattoo
    template_name = 'tattoo_list.html'


class TattooSearch(ListView):
    model = Tattoo
    template_name = 'tattoo_search.html'

    def get_queryset(self):

        categorias = Categoria.objects.all()
        return Tattoo.objects.filter(categoria=self.kwargs['categoria'])


class TattooCreate(CreateView):
    model = Tattoo
    form_class = TattooForm
    template_name = 'tattoo_form.html'
    success_url = reverse_lazy('index')


class TattooUpdate(UpdateView):
    model = Tattoo
    form_class = TattooForm
    template_name = 'tattoo_form.html'
    success_url = reverse_lazy('index')


class CommentCreate(CreateView):
    model = Comentario
    form_class = CommentForm
    template_name = 'tattoo_comment.html'
    success_url = reverse_lazy('index')
