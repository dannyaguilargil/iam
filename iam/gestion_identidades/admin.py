from django.contrib import admin
from .models import  aplicativo,modulo, solicitud, respuestasolicitud
from django.contrib.sessions.models import Session
from django.contrib.admin.models import LogEntry

admin.site.register(Session)


class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('action_time', 'user', 'content_type', 'object_repr', 'action_flag', 'change_message')
    list_filter = ('action_flag', 'user')
    search_fields = ('object_repr', 'change_message')
admin.site.register(LogEntry, LogEntryAdmin)


class Aplicativo(admin.ModelAdmin):
    list_display=('id', 'nombre', 'activo', 'fecha_creacion','fecha_actualizacion')
    search_fields = ('nombre',)
admin.site.register(aplicativo, Aplicativo)

class Modulo(admin.ModelAdmin):
    list_display=('id', 'aplicativo', 'nombre', 'activo', 'fecha_creacion', 'fecha_actualizacion')
    list_filter = ('aplicativo', 'fecha_creacion')
    search_fields = ('nombre',)
admin.site.register(modulo, Modulo)

class Solicitud(admin.ModelAdmin):
    list_display=('id', 'nombre', 'descripcion', 'estructura_json', 'fecha_creacion', 'fecha_actualizacion')
admin.site.register(solicitud, Solicitud)

class RespuestaSolicitud(admin.ModelAdmin):
    list_display=('id', 'solicitud', 'datos', 'fecha_creacion', 'fecha_actualizacion')
    list_filter = ('fecha_creacion',)
    search_fields = ('datos',)
admin.site.register(respuestasolicitud, RespuestaSolicitud)
