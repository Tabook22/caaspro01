from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import PeerReg
from .forms import PeerRegForm
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView
# to save the file in the filesytem not in the database
#from django.core.files.storage import FileSystemStorage


# Create your views here.
class peer_reg(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': PeerRegForm()}
        return render(request, 'attendance/attendance_add.html', context)

    def post(self, request, *args, **kwargs):
        #form = BlogEditForm(request.POST, request.FILES, instance=blog)
        form = PeerRegForm(request.POST, request.FILES)
        if form.is_valid():
            peer = form.save()
            peer.save()
            return HttpResponseRedirect(reverse_lazy('attendance:peer_reg_list'))
        return render(request, 'attendance/attendance_add.html', {'form': form})

class peer_reg_list(ListView):
    pass