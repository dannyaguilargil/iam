# forms.py
from django import forms
from .models import solicitud
from django_json_widget.widgets import JSONEditorWidget

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = solicitud
        fields = '__all__'
        widgets = {
            'estructura_json': JSONEditorWidget  # Editor visual para el JSON
        }
