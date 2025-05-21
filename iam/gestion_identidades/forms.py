from django_form_builder.forms import BaseDynamicForm
from collections import OrderedDict

class FormularioDinamico(BaseDynamicForm):
    def __init__(self, *args, estructura=None, **kwargs):
        super().__init__(*args, **kwargs)
        if estructura:
            estructura_dict = OrderedDict(estructura)
            self.build_fields(estructura_dict)
