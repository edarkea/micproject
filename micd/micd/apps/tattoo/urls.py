from django.urls import path
from micd.apps.tattoo.views import TattooList, ProductCreate

urlpatterns = [
    path('list', TattooList.as_view(), name='list_tattoo'),
    path('add', ProductCreate.as_view(), name='create_tattoo'),
]