# forms.py
from django import forms
from .models import solicitud, respuestasolicitud
from django_json_widget.widgets import JSONEditorWidget

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = solicitud
        fields = '__all__'
        widgets = {
            'estructura_json': JSONEditorWidget  
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'json_data' in kwargs:
            json_data = kwargs.pop('json_data')
            self.build_dynamic_fields(json_data)

    def build_dynamic_fields(self, json_data):
        for field_name, field_json in json_data.items():
            field_type = field_json.get('type')
            if field_type == 'select':
                choices = [(opt['value'], opt['label']) for opt in field_json['options']]
                self.fields[field_name] = forms.ChoiceField(
                    label=field_json['label'],
                    choices=choices,
                    widget=forms.Select,
                    required=field_json.get('required', True)
                )
            elif field_type == 'text':
                self.fields[field_name] = forms.CharField(
                    label=field_json['label'],
                    required=field_json.get('required', True)
                )
            elif field_type == 'email':
                self.fields[field_name] = forms.EmailField(
                    label=field_json['label'],
                    required=field_json.get('required', True)
                )
            elif field_type == 'password':
                self.fields[field_name] = forms.CharField(
                    label=field_json['label'],
                    required=field_json.get('required', True),
                    widget=forms.PasswordInput
                )

class RespuestaSolicitudForm(forms.ModelForm):
    class Meta:
        model = respuestasolicitud
        fields = '__all__'
        widgets = {
            'datos': JSONEditorWidget  
        }

class DynamicForm(forms.Form):
    def __init__(self, fields_json, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in fields_json:
            field_type = field.get('type')
            name = field.get('name')
            label = field.get('label')
            required = field.get('required', True)

            if field_type == 'text':
                self.fields[name] = forms.CharField(label=label, required=required)
            elif field_type == 'email':
                self.fields[name] = forms.EmailField(label=label, required=required)
            elif field_type == 'password':
                self.fields[name] = forms.CharField(label=label, required=required, widget=forms.PasswordInput)
            elif field_type == 'select':
                choices = [(opt['value'], opt['label']) for opt in field.get('options', [])]
                self.fields[name] = forms.ChoiceField(
                    label=label,
                    required=required,
                    choices=choices,
                    widget=forms.Select
                )
            # ...otros tipos si los tienes...

