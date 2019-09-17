from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Peertotur, Peertoturfile
from .forms import PeertoturForm, FileForm
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView
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
    print(uploadedfiles)
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
   #model=Peertotur
    form_class=PeertoturForm # because if am going to use the form i have to close the fields forms and fields can't be used at the same time
    template_name="peertotur/add_peertotur.html"
    #fields=['pname','paddress','pemail','pmajor','pdep','pgpamajor','pgpacum','pexgraduate','ptel','pgsm','yearofstudy','pimg']
    #success_url = reverse_lazy('peertotur:peertotur_list')
    queryset = Peertotur.objects.all()

    def from_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

# Notice: the primary funciton of DetailView is to redern view from a specific object
class peertotur_detail(DetailView):
    template_name="peertotur/peertotur_detail.html"
    context_object_name="peer"
    #queryset=Peertotur.objects.all() # there is not need for this because inside urls.py we changed the <int:pk> to <int:id>, and then we have the use the bellow function 
    # def get_object(self), which will return to us the needed record based up on the id we obtained from the url
    # if we are need to use querset=Peeertotur.objects.all() then we have to change back <int:pk> and not use the def get_object(self) method

    def get_object(self):
            id_=self.kwargs.get("id") #this is the actual id which passed through the url
            return get_object_or_404(Peertotur, id=id_)

class peertotur_list(ListView):
    model=Peertotur
    templat_name="peertotur/peertotur_list.html"
    #peertoturlist=Peertotur.objects.get()
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

class peertotur_update(UpdateView):
    #model=Peertotur
    template_name="peertotur/peertotur_update.html"
    form_class= PeertoturForm
    #context_object_name="peer"
    #fields=['pname','paddress','pemail','pmajor','pdep','pgpamajor','pgpacum','pexgraduate','ptel','pgsm','yearofstudy','pimg']
    success_url = reverse_lazy('peertotur:peertotur_list')

    def get_object(self):
        id=self.kwargs.get("id")
        return get_object_or_404(Peertotur, id=id)

    def form_valid(self, form):
        return super().form_valid(form)

    # def get_object(self):
        #id=self.kwargs.get("id")
       # return get_object_or_404(Peertotur, id=id)


class uploadfiles(CreateView):
    model: Peertoturfile
    form_class = FileForm
    # Here also we can use the following fields
    #fields = ['fname', 'filepath']
    success_url = 'upload_list'
    template_name = 'peertotur/upload_file.html'
    queryset = Peertoturfile.objects.all()
