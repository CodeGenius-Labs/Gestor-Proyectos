# Generated by Django 5.1 on 2024-10-08 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0003_archivos_tamaño_archivos_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivos',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
