from django.db import models
from datetime import datetime

class Cliente(models.Model):
    cliente_id = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    alerta = models.BooleanField(default=False)
    email = models.CharField(max_length=500)
    latitud = models.CharField(max_length=200, blank=True)
    longitud = models.CharField(max_length=200, blank=True)
    telefono = models.CharField(max_length=20)
    descripción = models.TextField(blank=True)
    logo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    fecha_de_alta = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.nombre
