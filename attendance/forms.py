from django import forms
from django.urls import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field, HTML,Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from .models import PeerReg

class PeerRegForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PeerRegForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'frmreg'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('attendance:attendance_add')
        self.helper.layout = Layout(
            Row(
                Column('pname', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
             Row(
                Column('datein', css_class='form-group col-md-4 mb-0'),
                Column('timein', css_class='form-group col-md-4 mb-0'),
                Column('timeout', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
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
        model = PeerReg
        fields = [
            'pname',
            'datein',
            'timein',
            'timeout'
        ]


