from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Peertotur, Peertoturfile, Peertoturexperties, Document, Peertoturq
from .forms import PeertoturForm, FileForm, PeertoturExpForm, attachmentForm, PeertoturqsForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView
# to save the file in the filesytem not in the database
from django.core.files.storage import FileSystemStorage

from .filters import PeerFilter, PeerExpFilter, PeerUploadFileFilter


class PeerFilterListView(ListView):
    model: Peertotur
    templat_name = "peertotur/peertotur_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)
        context['filter'] = PeerFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


class PeerExpFilterListView(ListView):
    model: Peertoturexperties
    templat_name = "peertotur/peertotur_exp_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)
        context['filter'] = PeerExpFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


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
    if request.method == "POST":
        peertoturfile = Peertoturfile.objects.get(pk=pk)
        peertoturfile.delete()
    return redirect('peertotur:upload_list')


class add_peertotur(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': PeertoturForm()}
        return render(request, 'peertotur/add_peertotur.html', context)

    def post(self, request, *args, **kwargs):
        #form = BlogEditForm(request.POST, request.FILES, instance=blog)
        form = PeertoturForm(request.POST, request.FILES)
        if form.is_valid():
            peer = form.save()
            peer.save()
            return HttpResponseRedirect(reverse_lazy('peertotur:peertotur_list'))
        return render(request, 'peertotur/peertotur_list.html', {'form': form})

    # model=Peertotur
    # form_class=PeertoturForm # because if am going to use the form i have to close the fields forms and fields can't be used at the same time
    # template_name="peertotur/add_peertotur.html"
    # #fields=['pname','paddress','pemail','pmajor','pdep','pgpamajor','pgpacum','pexgraduate','ptel','pgsm','yearofstudy','pimg']
    # #success_url = reverse_lazy('peertotur:peertotur_list')
    # queryset = Peertotur.objects.all()
    # def from_valid(self, form):
    #     #print(form.instance.user)=request.user # the user
    #     return super().form_valid(form)

# Notice: the primary funciton of DetailView is to redern view from a specific object

class peertotur_detail(DetailView):
    template_name = "peertotur/peertotur_detail.html"
    context_object_name = "peer"
    # queryset=Peertotur.objects.all() # there is not need for this because inside urls.py we changed the <int:pk> to <int:id>, and then we have the use the bellow function
    # def get_object(self), which will return to us the needed record based up on the id we obtained from the url
    # if we are need to use querset=Peeertotur.objects.all() then we have to change back <int:pk> and not use the def get_object(self) method

    def get_object(self):
        # this is the actual id which passed through the url
        id_ = self.kwargs.get("id")
        return get_object_or_404(Peertotur, id=id_)

class peertotur_list(ListView):
    # The Django ListView class comes with built-in support for pagination so all we need to do
    # is take advantage of it. Pagination is controlled by the GET parameter that controls
    # which page to show.

    model = Peertotur
    templat_name = "peertotur/peertotur_list.html"
    context_object_name = "peertoturlist"
    # paginate_by takes an integer specifying how many objects should be displayed per page.
    # If this is given, the view will paginate objects with paginate_by objects per page.
    # The view will expect either a page query string parameter (via request.GET) or a page
    # variable specified in the URLconf.
    paginate_by = 5
    # I can also use filter
    #queryset = Peertotur.objects.filter(pmajor="computer science").order_by('-reqdate')
    queryset = Peertotur.objects.all()  # Default: Model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)
        context['filter'] = PeerFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


class peertotur_delete(DeleteView):
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    # model = Peertotur
    # templat_name = "peertotur/peertotur_delete.html"
    # context_object_name = "peer"
    # success_url = reverse_lazy('peertotur:peertotur_list')


class peertoturexp_delete(DeleteView):
    # here we are deleting without confirmation page, we did the confirmation using jquery in the html page,
    # becausse get method will call for the confirmation page, and the post method will do the deletion
    model = Peertoturexperties
    success_url = success_url = reverse_lazy("peertotur:peertotur_exp_list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    # if we used the following code this will use a confirmation page
    # model = Peertoturexperties
    # # templat_name = "peertotur/peertoturexperties_confirm_delete.html"
    # success_url = reverse_lazy('peertotur:peertotur_exp_list')


class uploadfilelst(ListView):
    model = Peertoturfile
    template_name = 'peertotur/upload_list.html'
    context_object_name = 'uploadedfiles'


class peertotur_update(UpdateView):
    # model=Peertotur
    template_name = "peertotur/peertotur_update.html"
    form_class = PeertoturForm
    # context_object_name="peer"
    # fields=['pname','paddress','pemail','pmajor','pdep','pgpamajor','pgpacum','pexgraduate','ptel','pgsm','yearofstudy','pimg']
    success_url = reverse_lazy('peertotur:peertotur_list')

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Peertotur, id=id)

    def form_valid(self, form):
        return super().form_valid(form)

    # def get_object(self):
        # id=self.kwargs.get("id")
        # return get_object_or_404(Peertotur, id=id)


class peertoturexp_update(UpdateView):
    # model=Peertotur
    template_name = "peertotur/peertoturexp_update.html"
    form_class = PeertoturExpForm
    # context_object_name="peer"
    # fields=['pname','paddress','pemail','pmajor','pdep','pgpamajor','pgpacum','pexgraduate','ptel','pgsm','yearofstudy','pimg']
    success_url = reverse_lazy('peertotur:peertotur_exp_list')

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Peertoturexperties, id=id)

    def form_valid(self, form):
        return super().form_valid(form)

    # def get_object(self):
        # id=self.kwargs.get("id")
        # return get_object_or_404(Peertotur, id=id)


class peertotur_experties(CreateView):

    def get(self, request, *args, **kwargs):
        context = {'form': PeertoturExpForm()}
        return render(request, 'peertotur/peertotur_experties.html', context)

    def post(self, request, *args, **kwargs):
        #form = BlogEditForm(request.POST, request.FILES, instance=blog)
        form = PeertoturExpForm(request.POST)

        if form.is_valid():
            peer = form.save()
            peer.save()
            return HttpResponseRedirect(reverse_lazy('peertotur:peertotur_experties'))

        return render(request, 'peertotur/peertotur_experties.html', {'form': form})


class peertotur_exp_list(ListView):
    model = Peertoturexperties
    # Default: <app_label>/<model_name>_list.html
    template_name = 'peertotur/peertotur_exp_list.html'
    context_object_name = 'peerexp'  # Default: object_list
    paginate_by = 5

    queryset = Peertoturexperties.objects.all()  # Default: Model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)
        context['filterexp'] = PeerExpFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


class uploadfiles(CreateView):
    model: Peertoturfile
    form_class = FileForm
    # Here also we can use the following fields
    #fields = ['fname', 'filepath']
    success_url = 'upload_list'
    template_name = 'peertotur/upload_file.html'
    queryset = Peertoturfile.objects.all()

# uploading the peet toturs attachments


class document_detail(CreateView):
    #model = Document
    form_class = attachmentForm
    #fields = ['file']
    template_name = 'peertotur/document_detail.html'
    success_url = reverse_lazy('peertotur:document_detail')
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        print("-------------------in the name of god most merci most merciful-------------")
        form = self.form_class()
        getAll = Document.objects.all()
        return render(request, self.template_name, {'form': form, 'flist': getAll})

    def post(self, request, *args, **kwargs):
        print("-----allah----")
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            print("-----in the name of allah-----")
            # myfile = request.FILES['file']
            # fs = FileSystemStorage()
            # filename = fs.save(myfile.name, myfile)
            # uploaded_file_url = fs.url(filename)
            # print(uploaded_file_url)
            form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})
class document_detail_delete(DeleteView):
   # here we are deleting without confirmation page, we did the confirmation using jquery in the html page,
    # becausse get method will call for the confirmation page, and the post method will do the deletion
    model = Document
    success_url = success_url = reverse_lazy("peertotur:document_detail")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    # if we used the following code this will use a confirmation page
    # model = Peertoturexperties
    # # templat_name = "peertotur/peertoturexperties_confirm_delete.html"
    # success_url = reverse_lazy('peertotur:peertotur_exp_list')

class peertotur_qs_list(CreateView):
    model = Peertoturq
    form_class = PeertoturqsForm
    #fields = ['file']
    template_name = 'peertotur/peertotur_qs_list.html'
    success_url = reverse_lazy('peertotur:peertotur_qs_list')
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        form = self.form_class()
       # getAll = Peertoturq.objects.all()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            # myfile = request.FILES['file']
            # fs = FileSystemStorage()
            # filename = fs.save(myfile.name, myfile)
            # uploaded_file_url = fs.url(filename)
            # print(uploaded_file_url)
            form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})

class peertotur_qs_update(UpdateView):
    #model = Peertoturq
    form_class = PeertoturqsForm
    success_url = success_url = reverse_lazy("peertotur:peertotur_qs_list")

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Peertoturq, id=id)

    def form_valid(self, form):
        return super().form_valid(form)

class peertotur_qs_delete(DeleteView):
    # here we are deleting without confirmation page, we did the confirmation using jquery in the html page,
    # becausse get method will call for the confirmation page, and the post method will do the deletion
    model = Peertoturq
    success_url = success_url = reverse_lazy("peertotur:peertotur_qs_list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    # if we used the following code this will use a confirmation page
    # model = Peertoturexperties
    # # templat_name = "peertotur/peertoturexperties_confirm_delete.html"
    # success_url = reverse_lazy('peertotur:peertotur_exp_list')


