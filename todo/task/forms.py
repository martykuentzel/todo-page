from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Task
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button, HTML
from crispy_forms.bootstrap import FormActions

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name']
        labels = {
            'name': _(''),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'name',
            FormActions(
    HTML("""<a class="btn btn-secondary" href="{% url 'task:index' %}">Cancel</a>"""),
    Submit('submit', 'Submit', css_class="btn btn-success btn-bloc"),
        ))