from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import PeerReg
#from .forms import PeertoturForm, FileForm, PeertoturExpForm, attachmentForm, PeertoturqsForm
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView
# to save the file in the filesytem not in the database
#from django.core.files.storage import FileSystemStorage


# Create your views here.
class peer_reg(CreateView):
    pass