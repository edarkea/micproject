from django.contrib import admin
from micd.apps.tattoo.models import Tattoo, Categoria, Comentario

# Register your models here.
admin.site.register(Tattoo)
admin.site.register(Categoria)
admin.site.register(Comentario)