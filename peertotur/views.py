from django.shortcuts import render
from .models import Peertoturfile
from .forms import FileForm
from django.core.files.storage import FileSystemStorage

def showfile(request):
    lastfile= Peertoturfile.objects.last()
    filepath= lastfile.filepath
    filename= lastfile.name
    form= FileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context= {'filepath': filepath,
              'form': form,
              'filename': filename
              }
    return render(request, 'peertutor/files.html', context)


def upload(request):
    context={}
    if request.method =="POST":
        uploaded_file= request.FILES['document']
        fs=FileSystemStorage()
        # here we save the file, in a folder, then we are going to display the file we just uploaded to the user
        fname=fs.save(uploaded_file.name, uploaded_file)
        #fs.save(uploaded_file.name, uploaded_file) #to save the file in the folder
        context['url']=fs.url(fname)
    return render(request, 'peertotur/upload.html', context)