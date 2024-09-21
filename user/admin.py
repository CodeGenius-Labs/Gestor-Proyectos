from django.contrib import admin
from .models import User, Proyecto, Roles, MiembrosProyectos, Archivos, Comentario

# Register your models here.

admin.site.register(User)

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin', 'progreso')

admin.site.register(Roles)

@admin.register(MiembrosProyectos)
class MiembrosProyectosAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'proyecto', 'rol')

@admin.register(Archivos)
class ArchivosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'proyecto', 'usuario')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('correo', 'comentario', 'fecha', 'proyecto')