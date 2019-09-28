from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import datetime  
# Create your models here.
class PeerReg(models.Model):
    pname = models.CharField(
        verbose_name="Name", max_length=200, null=True, blank=True)
    datein = models.DateTimeField(verbose_name="Time In",null=True, blank=True, default=datetime.now())
    dateout = models.DateTimeField(verbose_name="Time Out",null=True, blank=True, default=datetime.now())

    class Meta:
        ordering = ['-datein']  # ordring by reqdate descending

    def __str__(self):
        return self.pname