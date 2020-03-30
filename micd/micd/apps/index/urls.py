from django.urls import path
from micd.apps.index.views import index

urlpatterns = [
    path('',index,name='index'),
]