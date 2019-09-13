from django.shortcuts import render, redirect
from .models import Peertoturfile
from .forms import FileForm
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage


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
