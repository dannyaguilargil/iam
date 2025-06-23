from .models import Organizacion
from django.contrib import admin

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug', 'descripcion')
    filter_horizontal = ('owners', 'users')
admin.site.register(Organizacion, OrganizationAdmin)