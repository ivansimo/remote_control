from django.db import models
from datetime import datetime

class Device(models.Model):
    deviceid = models.CharField(max_length=500)
    type_communication = models.CharField(max_length=500)
    dev_range = models.FloatField()
    message = models.CharField(max_length=500, blank=True)
    active = models.BooleanField(default=False)
    alarm = models.BooleanField(default=False)
    def __str__(self):
        return self.deviceid
    