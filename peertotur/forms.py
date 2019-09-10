from django import forms
from .models import Peertoturfile
class FileForm(forms.ModelForm):
    class Meta:
        model= Peertoturfile
        fields= ["fname", "filepath"]