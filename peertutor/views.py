from django.shortcuts import render
from .models import Peertoturfile
from .forms import FileForm

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