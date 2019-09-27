from django.contrib import admin
from .models import Peertotur, Peertoturexperties, Peertoturq, Peertoturfile, Document

# Register your models here.
admin.site.register(Peertotur)
admin.site.register(Peertoturexperties)
admin.site.register(Peertoturq)
admin.site.register(Peertoturfile)
admin.site.register(Document)
