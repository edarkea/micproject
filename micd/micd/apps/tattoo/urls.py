from django.urls import path
from micd.apps.tattoo.views import TattooList

urlpatterns = [
    path('list', TattooList.as_view(), name='list_tattoo'),
]