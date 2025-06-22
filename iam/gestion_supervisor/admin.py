from django.contrib import admin
from .models import supervisor
# Register your models here.
class Supervisor(admin.ModelAdmin):
    list_display = ('get_nombre_completo', 'cargo','fecha_creacion','fecha_actualizacion')
    search_fields = ('usuario__username', 'usuario__first_name', 'usuario__last_name')  # Para buscar por nombre o apellido

    def get_nombre_completo(self, obj):
        return obj.usuario.get_full_name()  # Obtiene el nombre completo del usuario
    get_nombre_completo.short_description = 'Nombre completo'  # Para mostrar el nombre de la columna en el panel

admin.site.register(supervisor, Supervisor)