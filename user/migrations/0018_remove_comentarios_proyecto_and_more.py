# Generated by Django 5.1 on 2024-09-24 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_remove_archivos_ruta_archivos_archivoss'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentarios',
            name='proyecto',
        ),
        migrations.RemoveField(
            model_name='comentarios',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='miembrosproyectos',
            name='proyecto',
        ),
        migrations.RemoveField(
            model_name='miembrosproyectos',
            name='rol',
        ),
        migrations.RemoveField(
            model_name='miembrosproyectos',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Archivos',
        ),
        migrations.DeleteModel(
            name='Comentarios',
        ),
        migrations.DeleteModel(
            name='Proyecto',
        ),
        migrations.DeleteModel(
            name='Roles',
        ),
        migrations.DeleteModel(
            name='MiembrosProyectos',
        ),
    ]