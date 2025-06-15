from django.db import models
import uuid
# Create your models here.
class aplicativo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, verbose_name='Nombre del aplicativo')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    

class modulo(models.Model):
    id = models.AutoField(primary_key=True)
    aplicativo=models.ForeignKey(aplicativo,null=True,blank=True,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, verbose_name='Nombre del modulo')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
    
class solicitud(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, verbose_name="Descripcion del formulario")
    estructura_json = models.JSONField(help_text="JSON que define los campos del formulario")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    def __str__(self):
        return self.nombre
    
class respuestasolicitud(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    solicitud = models.ForeignKey('solicitud', on_delete=models.CASCADE, related_name='respuestas')
    datos = models.JSONField(help_text="Respuestas del formulario en formato JSON")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    def __str__(self):
        return f"Respuesta a {self.solicitud.nombre}"
    
#class respuesta(models.Model):
#    formulario = models.ForeignKey(formulario, on_delete=models.CASCADE, related_name='respuestas')
#    datos = models.JSONField(help_text="Respuestas en formato JSON")
#    fecha_envio = models.DateTimeField(auto_now_add=True)