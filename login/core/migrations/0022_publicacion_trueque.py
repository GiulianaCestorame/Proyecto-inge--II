# Generated by Django 5.0.6 on 2024-06-05 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_remove_trueque_creado_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='trueque',
            field=models.BooleanField(default=False),
        ),
    ]
