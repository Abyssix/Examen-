from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Casa(models.Model):
    DISPONIBILIDAD_CHOICES = [
        ('disponible', 'Disponible'),
        ('no_disponible', 'No disponible'),
    ]
        
    id_casa = models.AutoField(db_column='idcasa', primary_key=True)
    ubicacion = models.CharField(max_length=100, blank=False, null=False)
    precio = models.FloatField(blank=False, null=False)
    disponibilidad = models.CharField(
        max_length=15,
        choices=DISPONIBILIDAD_CHOICES,
        default='disponible',
    )
    imagen = models.CharField(max_length=2083, blank=False, null=False)


class Arriendo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE)
    fecha_arriendo = models.DateField(auto_now_add=True)
    dias_arriendo = models.PositiveIntegerField()