from django import forms
from django.urls import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field
from .models import Peertotur, Peertoturfile

class PeertoturForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PeertoturForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('peertotur:peertotur_list')
        self.helper.layout = Layout(
            Row(
                Column('pname', css_class='form-group col-md-6 mb-0'),
                Column('paddress', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('pemail',css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('pmajor',css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('pdep', css_class='form-group col-md-3 mb-0'),
                Column('pgpacum', css_class='form-group col-md-3 mb-0'),
                Column('pexgraduate', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('ptel',css_class='form-group col-md-3 mb-0'),
                 Column('pgsm',css_class='form-group col-md-3 mb-0'),
               Column('yearofstudy',css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

             'pimg',
            Submit('submit', 'Sign in')
        )
    
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
