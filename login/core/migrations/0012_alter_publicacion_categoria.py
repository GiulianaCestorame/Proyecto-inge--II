# Generated by Django 5.0.6 on 2024-05-14 22:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_categoria_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.categoria'),
        ),
    ]
