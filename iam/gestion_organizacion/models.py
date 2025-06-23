from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Organizacion(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    owners = models.ManyToManyField(
        User,
        related_name='owned_organizations',
        blank=True,
        help_text="Usuarios que administran esta organización"
    )

    users = models.ManyToManyField(
        User,
        related_name='organizations',
        blank=True,
        help_text="Miembros normales de la organización"
    )

    def __str__(self):
        return self.nombre