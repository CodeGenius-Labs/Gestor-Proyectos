# Generated by Django 5.1 on 2024-09-23 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_alter_comentarios_fecha_hora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archivos',
            name='ruta',
        ),
        migrations.AddField(
            model_name='archivos',
            name='archivoss',
            field=models.FileField(default='archivos/prueba.txt', upload_to='archivos/'),
        ),
    ]