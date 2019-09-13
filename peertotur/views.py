from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Peertotur, Peertoturfile
from .forms import PeertoturForm, FileForm
from django.views.generic import TemplateView, ListView, CreateView, DeleteView
from django.core.files.storage import FileSystemStorage # to save the file in the filesytem not in the database


def showfile(request):
    lastfile = Peertoturfile.objects.last()
    filepath = lastfile.filepath
    filename = lastfile.name
    form = FileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context = {'filepath': filepath,
               'form': form,
               'filename': filename
               }
    return render(request, 'peertutor/files.html', context)


def upload(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        # here we save the file, in a folder, then we are going to display the file we just uploaded to the user
        fname = fs.save(uploaded_file.name, uploaded_file)
        # fs.save(uploaded_file.name, uploaded_file) #to save the file in the folder
        context['url'] = fs.url(fname)
    return render(request, 'peertotur/upload.html', context)


def upload_list(request):
    uploadedfiles = Peertoturfile.objects.all()
    return render(request, 'peertotur/upload_list.html', {'uploadedfiles': uploadedfiles})


def upload_file(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_list.html')
    else:
        form = FileForm()

    context = {}
    context['form'] = form
    return render(request, 'peertotur/upload_file.html', context)

def upload_delete(request, pk):
    if request.method=="POST":
        peertoturfile=Peertoturfile.objects.get(pk=pk)
        peertoturfile.delete()
    return redirect('peertotur:upload_list')

class add_peertotur(CreateView):
    model=Peertotur
    #form_class=PeertoturForm # because if am going to use the form i have to close the fields forms and fields can't be used at the same time
    template_name="peertotur/add_peertotur.html"
    fields=['pname','paddress','pemail','pmajor','pdep','pgpamajor','pgpacum','pexgraduate','ptel','pgsm','yearofstudy','pimg']
    success_url = reverse_lazy('peertotur:peertotur_list')
    template_name = 'peertotur/add_peertotur.html'
    queryset = Peertotur.objects.all()

class peertotur_list(ListView):
    model=Peertotur
    templat_name="peertotur/peertotur_list.html"
    context_object_name="peertoturlist"

class peertotur_delete(DeleteView):
    model=Peertotur
    templat_name="peertotur/peertotur_delete.html"
    context_object_name="peer"
    success_url = reverse_lazy('peertotur:peertotur_list')

class uploadfilelst(ListView):
    model = Peertoturfile
    template_name = 'peertotur/upload_list.html'
    context_object_name = 'uploadedfiles'


class uploadfiles(CreateView):
    model: Peertoturfile
    form_class = FileForm
    # Here also we can use the following fields
    #fields = ['fname', 'filepath']
    success_url = 'upload_list'
    template_name = 'peertotur/upload_file.html'
    queryset = Peertoturfile.objects.all()
