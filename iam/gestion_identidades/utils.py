# utils.py
from django import forms

def generar_formulario_dinamico(estructura_json):
    class FormularioDinamico(forms.Form):
        pass

    for campo in estructura_json:
        field_type = campo.get("type", "text")
        field_name = campo.get("name")
        field_label = campo.get("label", field_name)
        required = campo.get("required", False)

        if field_type == "text":
            field = forms.CharField(label=field_label, required=required)
        elif field_type == "email":
            field = forms.EmailField(label=field_label, required=required)
        elif field_type == "password":
            field = forms.CharField(label=field_label, required=required, widget=forms.PasswordInput)
        elif field_type == "integer":
            field = forms.IntegerField(label=field_label, required=required)
        elif field_type == "select_one":
            choices = [(opt, opt) for opt in campo.get("choices", [])]
            field = forms.ChoiceField(label=field_label, required=required, choices=choices)
        else:
            field = forms.CharField(label=field_label, required=required)

        FormularioDinamico.base_fields[field_name] = field

    return FormularioDinamico
