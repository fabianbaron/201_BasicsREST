from django.db import models


# Create your models here.
class Empleados(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    identificacion = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
