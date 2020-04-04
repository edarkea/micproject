from django.urls import path
from micd.apps.tattoo.views import TattooList, TattooCreate, TattooSearch, TattooUpdate, CommentCreate

urlpatterns = [
    path('list', TattooList.as_view(), name='list_tattoo'),
    path('add', TattooCreate.as_view(), name='create_tattoo'),
    path('search/<int:categoria>', TattooSearch.as_view(), name='search_tattoo'),
    path('edit/<int:pk>', TattooUpdate.as_view(), name='edit_tattoo'),
    path('comment/<int:pk>', CommentCreate.as_view(), name='comment_tattoo'),
]