# Generated by Django 5.0.4 on 2024-05-31 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_trueque_confirmado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trueque',
            name='creado_en',
        ),
        migrations.AddField(
            model_name='trueque',
            name='fecha_efectivizacion',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
