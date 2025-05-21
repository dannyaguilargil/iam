from django.db import models

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
    
class Formulario(models.Model):
    nombre = models.CharField(max_length=100)
    estructura = models.JSONField(help_text="Define aquí la estructura del formulario (JSON)")