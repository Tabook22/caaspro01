from django import forms
from django.urls import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field
from .models import Peertotur, Peertoturfile, Peertoturexperties, Document


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
                Column('pemail', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('pmajor', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('pdep', css_class='form-group col-md-3 mb-0'),
                Column('pgpacum', css_class='form-group col-md-3 mb-0'),
                Column('pexgraduate', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('ptel', css_class='form-group col-md-3 mb-0'),
                Column('pgsm', css_class='form-group col-md-3 mb-0'),
                Column('yearofstudy', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

            'pimg',
            Submit('submit', 'Sign in')
        )

    class Meta:
        model = Peertotur
        fields = [
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


class PeertoturExpForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PeertoturExpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('peertotur:peertotur_exp_list')
        self.helper.layout = Layout(
            Row(
                Column('pname', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('coursename', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('coursecode', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('fp', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Sign in')
        )

    class Meta:
        model = Peertoturexperties
        fields = [
            'pname',
            'coursename',
            'coursecode',
            'fp'
        ]


class PeertoturExpForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PeertoturExpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('peertotur:peertotur_experties')
        self.helper.layout = Layout(
            Row(
                Column('pname', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('coursename', css_class='form-group col-md-6 mb-0'),
                Column('coursecode', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('fp', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            # Row(
            #     Column('un',css_class='form-group col-md-12 mb-0'),
            #     css_class='form-row'
            # ),
            Submit('submit', 'Add area(s) of experties')
        )

    class Meta:
        model = Peertoturexperties
        fields = [
            'pname',
            'coursename',
            'coursecode',
            'fp'
        ]


class FileForm(forms.ModelForm):
    class Meta:
        model = Peertoturfile
        fields = ["fname", "filepath"]


class attachmentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ["pname", "file"]
   # file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
