from django import forms
from .models import Peertotur, Peertoturfile

class PeertoturForm(forms.ModelForm):
    class Meta:
        model=Peertotur
        fields=[
            'pname',
            'paddress',
            'pemail',
            'pmajor',
            'pdep',
            'pgpamajor',
            'pgpacum',
            'pexgraduate',
            'ptel',
            'pgsm',
            'yearofstudy',
            'pimg'
        ]

class FileForm(forms.ModelForm):
    class Meta:
        model = Peertoturfile
        fields = ["fname", "filepath"]
