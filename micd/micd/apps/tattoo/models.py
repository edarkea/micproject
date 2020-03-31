from django.db import models

# Create your models here.
class Tattoo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=16, decimal_places=2)
    imagen = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nombre