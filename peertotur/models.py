from django.db import models

# Create your models here.



class Peertotur(models.Model):
    yearofstudy_choices=[
        ('Soph','Sopph'),
        ('Jr','Jr'),
        ('Sr','Sr'),
        ('Grad_Student','Grad_Student'),
    ]

    pname=models.CharField(max_length=200)
    paddress=models.CharField(max_length=200)
    pemail=models.CharField(max_length=100)
    pmajor=models.CharField(max_length=100)
    pdep=models.CharField(max_length=100)
    pgpamajor=models.CharField(max_length=10)
    pgpacum=models.CharField(max_length=100)
    pexgraduate=models.IntegerField(max_length=4)
    reqdate=models.DateTimeField(auto_now=True)
    ptel=models.CharField(max_length=20)
    pgsm=models.CharField(max_length=20)
    yearofstudy=models.CharField(max_length=20, choices=yearofstudy_choices)
    #attchments=models.FileField(upload_to='files/', null=True, verbose_name="")
    pimg=models.ImageField(upload_to='peertoturs/img/', null=True, blank=True)
    def __str__(self):
        return self.pname

class Peertoturexperties(models.Model):
    pname=models.ForeignKey('Peertotur', on_delete=models.CASCADE)
    coursename=models.CharField(max_length=200)
    coursecode=models.CharField(max_length=10)
    fp=models.BooleanField(default=False)
    un=models.BooleanField(default=False)

    def __str__(self):
        return self.coursecode + " " + self.coursename

class Peertoturq(models.Model):
    pname=models.ForeignKey('Peertotur', on_delete=models.CASCADE)
    shortq=models.TextField()

class Peertoturfile(models.Model):
    #pname=models.ForeignKey('Peertotur', on_delete=models.CASCADE)
    fname= models.CharField(max_length=500)
    filepath= models.FileField(upload_to='peertoturs/uploads/', null=True, blank=True, verbose_name="")

    def __str__(self):
        return self.fname + ": " + str(self.filepath)