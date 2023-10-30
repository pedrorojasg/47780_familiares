from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    parentezco_conmigo = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    dni = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre} ({self.parentezco_conmigo})"
