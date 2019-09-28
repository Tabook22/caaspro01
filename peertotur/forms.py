from django import forms
from django.urls import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field, HTML,Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from .models import Peertotur, Peertoturfile, Peertoturexperties, Document, Peertoturq


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
            Submit('submit', 'Add')
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
            Submit('submit', 'Add')
        )

    class Meta:
        model = Peertoturexperties
        fields = [
            'pname',
            'coursename',
            'coursecode',
            'fp'
        ]


class PeertoturqsForm(forms.ModelForm):
    question1= forms.CharField(
        widget = forms.Textarea(),
    )
    question2= forms.CharField(
        widget = forms.Textarea(),
    )
    question3= forms.CharField(
        widget = forms.Textarea(),
    )
    def __init__(self, *args, **kwargs):
        super(PeertoturqsForm, self).__init__(*args, **kwargs)
        #setting the initial values for the fields
        self.fields['question1'].initial = 'List coursework you have completed that may be beneficial in your role as a tutor'
        self.fields['question2'].initial = 'List four abilities/skills that would make you an effective peer tutor'
        self.fields['question3'].initial = 'Describe the experiences and knowledge you have gained thus far in your undergraduate career that you would like to share with new students in your major.'
        self.helper = FormHelper(self)
        self.helper.form_id = 'frmqs'
        #self.helper.form_method = 'post'
        self.helper.form_action = reverse('peertotur:peertotur_qs_list')
        #self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
        #self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Row(
                Column(
                    HTML("""<p style="margin:20px;">We use these questions and answers to get better, <strong>please help us {{ username }}</˓→strong></p>"""),
                    css_class='form-row'
                )
            ),
            Row(
                Column('pname', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
             Row(
                Column(
                   Field('question1', rows="3", css_class='input-xlarge'), css_class='form-group col-md-6 mb-0'),
                Column('answer1', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column(Field('question2', rows="3", css_class='input-xlarge'), css_class='form-group col-md-6 mb-0'),
                Column('answer2', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column(Field('question3', rows="3", css_class='input-xlarge'), css_class='form-group col-md-6 mb-0'),
                Column('answer3', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            #FormActions: It wraps fields in a <div class="form-actions">. It is usually used to wrap form’s buttons:
            
            Row(
                Column(
                    FormActions(
                        Submit('submit', 'Save changes', css_class="btn-primary"),
                        Submit('cancel', 'Cancel'),css_class='btnnas'
                    ), css_class='form-group col-md-12 mb-0'
                ),
                css_class='form-row'
             )
            #Submit('submit', 'Add Q&A')
        )

    class Meta:
        model = Peertoturq
        fields = [
            'pname',
            'question1',
            'answer1',
            'question2',
            'answer2',
            'question3',
            'answer3',
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
        fields = ["pname","ftitle" ,"file"]
   # file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
