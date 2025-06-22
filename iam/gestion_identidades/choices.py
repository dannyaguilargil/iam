from django.db import models

class FormularioTipos(models.TextChoices):
    CREACION_USUARIO = 'creacion_usuario', 'Autoregistro'
    SOLICITAR_USUARIO = 'solicitar_usuario', 'Solicitar usuario en IAM'
    CREACION_IDENTIDADES = 'creacion_identidades', 'Formulario de gestion de identidades'
    CREACION_PAZ = 'creacion_paz', 'Formulario de paz y salvo'