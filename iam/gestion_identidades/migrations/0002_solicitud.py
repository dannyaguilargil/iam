# Generated by Django 5.2.1 on 2025-06-15 15:36

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_identidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='solicitud',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, verbose_name='Descripcion del formulario')),
                ('estructura_json', models.JSONField(help_text='JSON que define los campos del formulario')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
            ],
        ),
    ]
