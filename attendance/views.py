from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import PeerReg
from .forms import PeerRegForm
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView
# to save the file in the filesytem not in the database
#from django.core.files.storage import FileSystemStorage

from peertotur.filters import  PeerFilter
# Create your views here.
class attendance_add(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': PeerRegForm()}
        context['getAll']=PeerReg.objects.all()  # Default: Model.objects.all()
        return render(request, 'attendance/attendance_add.html', context)
    # model = PeerReg
    # fields=['datein','timein','timeout']
    # templat_name = "attendance/attendance_add.html"
    # context_object_name = "attlst"
    # queryset = PeerReg.objects.all()  # Default: Model.objects.all()
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(*kwargs)
    #     context['filter'] = PeerFilter(
    #         self.request.GET, queryset=self.get_queryset())
    #     return context

    def post(self, request, *args, **kwargs):
        #form = BlogEditForm(request.POST, request.FILES, instance=blog)
        form = PeerRegForm(request.POST, request.FILES)
        if form.is_valid():
            peer = form.save()
            peer.save()
            return HttpResponseRedirect(reverse_lazy('attendance:attendance_add'))
        return render(request, 'attendance/attendance_add.html', {'form': form})

class attendance_list(ListView):
    model = PeerReg
    templat_name = "attendance/attendance_list.html"
    context_object_name = "attlst"
    queryset = PeerReg.objects.all()  # Default: Model.objects.all()


class attendance_delete(DeleteView):
    model = PeerReg
    success_url = success_url = reverse_lazy("attendance:attendance_add")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
class attendance_detail(UpdateView):
    template_name = "attendance/attendance_detail.html"
    form_class = PeerRegForm
    success_url = reverse_lazy('attendance:attendance_add')

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(PeerReg, id=id)

    def form_valid(self, form):
        return super().form_valid(form)

    # def get_object(self):
        # id=self.kwargs.get("id")
        # return get_object_or_404(Peertotur, id=id)

    # template_name = "attendance/attendance_detail.html"
    # context_object_name = "att"
    
    # def get_object(self):
    #     # this is the actual id which passed through the url
    #     id_ = self.kwargs.get("id")
    #     return get_object_or_404(PeerReg, id=id_)