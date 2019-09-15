from django.db import models
from django.urls import reverse
# Create your models here.



class Peertotur(models.Model):
    yearofstudy_choices=[
        ('Soph','Sopph'),
        ('Jr','Jr'),
        ('Sr','Sr'),
        ('Grad_Student','Grad_Student'),
    ]

    pname=models.CharField(verbose_name="Name", max_length=200)
    paddress=models.CharField(verbose_name="Address",max_length=200)
    pemail=models.CharField(verbose_name="E-mail address", max_length=100)
    pmajor=models.CharField(verbose_name="Major",max_length=100)
    pdep=models.CharField(verbose_name="Department",max_length=100)
    pgpamajor=models.CharField(verbose_name="GPA in major",max_length=10)
    pgpacum=models.CharField(verbose_name="Cumulative GPA",max_length=100)
    pexgraduate=models.DateField(verbose_name="Expected date of Graduation (mm/dd/YYYY)", auto_now_add=False, auto_now=False, blank=True)
    reqdate=models.DateTimeField(auto_now_add=True)
    ptel=models.CharField(verbose_name="Tel",max_length=20)
    pgsm=models.CharField(verbose_name="GSM",max_length=20)
    yearofstudy=models.CharField(verbose_name="Year of Study",max_length=20, choices=yearofstudy_choices)
    #attchments=models.FileField(upload_to='files/', null=True, verbose_name="")
    pimg=models.ImageField(verbose_name="Image",upload_to='peertoturs/img/', null=True, blank=True) # null let it be null on the database and the blank let let it be blank on the form, because we have form validation, someime it will not allow blancks
    
    def __str__(self):
        return self.pname

    #here we use this to delete the uploaded peertotur images
    def delete(self, *args, **kwargs):
        self.pimg.delete()
        super().delete(*args, **kwargs)
    
    #this means after i created a new peertotur i will be transfered to the newlly created peertotur, but i can override it by
    #success_url="/" for example this will be inside the peertotur_create view it self inside the view.py fiel
    #also i can use"
    #                def_success_url(self): 
                        #return '/'
    def get_absolute_url(self):
        #here the reverse function is to go to peertotur_detail view
        return reverse('peertotur:peertotur_detail', kwargs={'pk': self.pk})

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
    
    #here we use this to delete the uploaded files
    def delete(self, *args, **kwargs):
        self.filepath.delete()
        super().delete(*args, **kwargs)