from django.contrib import admin
from .models import  aplicativo,modulo
#from import_export.admin import ImportExportModelAdmin
#from import_export.resources import ModelResource
#from import_export.admin import ExportMixin
#from import_export.admin import ImportExportModelAdmin
####PARA EL REENVIO DE APROBADOS###
#from django.core.mail import send_mail
#from django.core.mail import EmailMultiAlternatives

class Aplicativo(admin.ModelAdmin):
    list_display=('id', 'nombre', 'activo', 'fecha_creacion','fecha_actualizacion')
    search_fields = ('nombre',)
admin.site.register(aplicativo, Aplicativo)

class Modulo(admin.ModelAdmin):
    list_display=('id', 'aplicativo', 'nombre', 'activo', 'fecha_creacion', 'fecha_actualizacion')
    list_filter = ('aplicativo', 'fecha_creacion')
    search_fields = ('nombre',)
admin.site.register(modulo, Modulo)