from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.


class Peertotur(models.Model):
    yearofstudy_choices = [
        ('Soph', 'Sopph'),
        ('Jr', 'Jr'),
        ('Sr', 'Sr'),
        ('Grad_Student', 'Grad_Student'),
    ]

    pname = models.CharField(
        verbose_name="Name", max_length=200, null=True, blank=True)
    paddress = models.CharField(
        verbose_name="Address", max_length=200, null=True, blank=True)
    pemail = models.CharField(
        verbose_name="E-mail address", max_length=100, null=True, blank=True)
    pmajor = models.CharField(verbose_name="Major",
                              max_length=100, null=True, blank=True)
    pdep = models.CharField(verbose_name="Department",
                            max_length=100, null=True, blank=True)
    pgpamajor = models.CharField(
        verbose_name="GPA in major", max_length=10, null=True, blank=True)
    pgpacum = models.CharField(
        verbose_name="Cumulative GPA", max_length=10, null=True, blank=True)
    pexgraduate = models.CharField(
        verbose_name="Expected date of Graduation", max_length=20, null=True, blank=True)
    reqdate = models.DateTimeField(auto_now_add=True)
    ptel = models.CharField(
        verbose_name="Tel", max_length=20, null=True, blank=True)
    pgsm = models.CharField(
        verbose_name="GSM", max_length=20, null=True, blank=True)
    yearofstudy = models.CharField(
        verbose_name="Year of Study", max_length=20, choices=yearofstudy_choices, null=True, blank=True)
    #attchments=models.FileField(upload_to='files/', null=True, verbose_name="")
    # null let it be null on tshe database and the blank let let it be blank on the form, because we have form validation, someime it will not allow blancks
    pimg = models.ImageField(
        verbose_name="Peer Totur Image", upload_to='peertoturs/img/%Y/%m/%d', null=True, blank=True)

    class Meta:
        ordering = ['-reqdate']  # ordring by reqdate descending

    def __str__(self):
        return self.pname

    # here we use this to delete the uploaded peertotur images
    def delete(self, *args, **kwargs):
        self.pimg.delete()
        super().delete(*args, **kwargs)

    # this means after i created a new peertotur i will be transfered to the newlly created peertotur, but i can override it by
    # success_url="/" for example this will be inside the peertotur_create view it self inside the view.py fiel
    # also i can use"
    #                def_success_url(self):
        # return '/'
    def get_absolute_url(self):
        # here the reverse function is to go to peertotur_detail view
        return reverse('peertotur:peertotur_detail', kwargs={'pk': self.pk})


class Peertoturexperties(models.Model):
    pname = models.ForeignKey(
        'Peertotur', on_delete=models.CASCADE, verbose_name="Peer Totur List")
    coursename = models.CharField(
        verbose_name="Course Name", max_length=200, null=True, blank=True)
    coursecode = models.CharField(
        verbose_name="Course Code", max_length=10, null=True, blank=True)
    fp = models.BooleanField(default=False, null=True, blank=True)
    # un = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        ordering = ['coursename']  # ordring by reqdate descending

    def __str__(self):
        return self.coursecode + " " + self.coursename

    # here we use this to delete the uploaded peertotur experties
    # def delete(self, *args, **kwargs):
    #     super().delete(*args, **kwargs)


class Peertoturq(models.Model):
    pname = models.ForeignKey('Peertotur', on_delete=models.CASCADE ,verbose_name="Peer Tutor Name")
    question1 = models.CharField(verbose_name="Question1",max_length=300, null=True, blank=True)
    answer1 = models.TextField(verbose_name="Answer1", null=True, blank=True)
    question2 = models.CharField(verbose_name="Question2",max_length=300, null=True, blank=True)
    answer2 = models.TextField(verbose_name="Answer2", null=True, blank=True)
    question3 = models.CharField(verbose_name="Question3",max_length=300, null=True, blank=True)
    answer3 = models.TextField(verbose_name="Answer3", null=True, blank=True)
    qsdate = models.DateTimeField(auto_now_add=True)


class Peertoturfile(models.Model):
    #pname=models.ForeignKey('Peertotur', on_delete=models.CASCADE)
    fname = models.CharField(max_length=500)
    filepath = models.FileField(
        upload_to='peertoturs/uploads/', null=True, blank=True, verbose_name="")

    def __str__(self):
        return self.fname + ": " + str(self.filepath)

    # here we use this to delete the uploaded files
    def delete(self, *args, **kwargs):
        self.filepath.delete()
        super().delete(*args, **kwargs)


class StudentComments(models.Model):
    mtitle = models.CharField(max_length=300, blank=True, null=True)
    mbody = models.CharField(max_length=300, null=True, blank=True)
    mstatus = models.BooleanField(default=False)
    mdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mtitle


class Document(models.Model):
    pname = models.ForeignKey('Peertotur', on_delete=models.CASCADE)
    ftitle=models.CharField(verbose_name="file title", max_length=200, null=True, blank=True)
    file = models.FileField(
        upload_to='peertoturs/docs/', null=True, blank=True)
    dateupload = models.DateTimeField(auto_now_add=True)

    @property
    def filename(self):
        name = self.file.name.split("/")[1].replace('_', ' ').replace('-', ' ')
        return name

    def get_absolute_url(self):
        return reverse('peertotur:document_detail', kwargs={'pk': self.pk})
