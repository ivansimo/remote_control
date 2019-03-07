from django.db import models
from datetime import datetime

class Jsonfile(models.Model):
    tipo = models.CharField(max_length=500, blank=True)
    designación = models.CharField(max_length=500, blank=True)
    contador_horario_grupo = models.CharField(max_length=500, blank=True)
    contador_horario_motor = models.DateTimeField(default=datetime.now, blank=True)
    nivel_fuel = models.DateTimeField(default=datetime.now, blank=True)
    temp_agua = models.CharField(max_length=200, blank=True)
    v_bat = models.CharField(max_length=200, blank=True)
    temp_aceite = models.BooleanField(default=False)
    presión_aceite_bar = models.DateTimeField(default=datetime.now, blank=True)
    frec_hz = models.CharField(max_length=200, blank=True)
    v1 = models.CharField(max_length=200, blank=True)
    p_kw = models.CharField(max_length=200, blank=True)
    q_kvar = models.CharField(max_length=200, blank=True)
    s_kvar = models.CharField(max_length=200, blank=True)
    tensión_ext = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.tipo