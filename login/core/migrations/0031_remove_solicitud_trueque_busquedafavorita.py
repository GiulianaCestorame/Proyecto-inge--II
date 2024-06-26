# Generated by Django 5.0.4 on 2024-06-12 03:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_categoria_estado_solicitud_trueque'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='trueque',
        ),
        migrations.CreateModel(
            name='BusquedaFavorita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('termino_busqueda', models.CharField(max_length=255)),
                ('fecha_guardada', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('usuario', 'termino_busqueda')},
            },
        ),
    ]
