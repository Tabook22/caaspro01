from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import datetime  
# Create your models here.
class PeerReg(models.Model):
    pname = models.ForeignKey('peertotur.Peertotur', on_delete=models.CASCADE, verbose_name="Peer Totur List")
    datein = models.CharField(verbose_name="Date In",max_length=20, null=True, blank=True)
    timein=models.CharField(verbose_name="Time In",max_length=20,null=True, blank=True)
    timeout=models.CharField(verbose_name="Time Out",max_length=20,null=True, blank=True)

    class Meta:
        ordering = ['-datein']  # ordring by reqdate descending

    def __str__(self):
        return self.pname