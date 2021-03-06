from django.db import models
from datetime import datetime

class Contact(models.Model):
    modelo = models.CharField(max_length=200)
    n_serie = models.IntegerField()
    nombrecontacto = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.nombrecontacto