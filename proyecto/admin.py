from django.contrib import admin
from .models import Proyecto, Roles, MiembrosProyectos, Archivos, Comentarios

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin', 'progreso')

admin.site.register(Roles)

@admin.register(MiembrosProyectos)
class MiembrosProyectosAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'proyecto', 'rol')

@admin.register(Archivos)
class ArchivosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'proyecto', 'usuario', 'archivoss')

@admin.register(Comentarios)
class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('comentario', 'proyecto', 'usuario', 'fecha_hora')
