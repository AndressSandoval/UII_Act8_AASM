from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Inventario(models.Model):
    nombre = models.CharField(max_length=50)
    anio = models.IntegerField()
    fecha = models.DateField(_(""), auto_now=False, auto_now_add=False)
    disponible = models.CharField(max_length=5)

    def __str__(self):
        return f'Inventario: {self.nombre} {self.anio}'