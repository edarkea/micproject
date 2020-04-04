from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+' '+str(self.id)


class Tattoo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=16, decimal_places=2)
    imagen = models.ImageField(blank=True, null=True)
    categoria = models.ForeignKey(
        Categoria, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


class Comentario(models.Model):
    isuario = models.CharField(max_length=50)
    comentario = models.CharField(max_length=250)
    tattoo = models.ForeignKey(
        Tattoo, null=True, blank=True, on_delete=models.DO_NOTHING)
