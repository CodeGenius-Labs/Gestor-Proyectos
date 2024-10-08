from django.db import models
from user.models import User
import mimetypes
import os  

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    progreso = models.IntegerField(default=0)

class Roles(models.Model):
    ADMIN_DEPARTAMENTO = 'Administrador del departamento'
    TUTOR = 'Tutor'
    ASISTENTE = 'Asistente'

    ROLE_CHOICES = [
        (ADMIN_DEPARTAMENTO, 'Administrador del departamento'),
        (TUTOR, 'Tutor'),
        (ASISTENTE, 'Asistente'),
    ]

    rol = models.CharField(max_length=50, choices=ROLE_CHOICES, default=TUTOR)
    
    def __str__(self):
        return self.rol

class MiembrosProyectos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    rol = models.ForeignKey(Roles, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario} - {self.rol} - {self.proyecto}"
    
class Archivos(models.Model):
    nombre = models.CharField(max_length=45)
    archivoss = models.FileField(upload_to='archivos/')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    tipo = models.CharField(max_length=100, blank=True)  # Campo para el tipo de archivo
    tamaño = models.PositiveIntegerField(default=0)  # Campo para el tamaño en KB

    def save(self, *args, **kwargs):
        # Almacenar el tipo y tamaño automáticamente al guardar el archivo
        if self.archivoss:
            # Obtener la extensión del archivo
            _, extension = os.path.splitext(self.archivoss.name)

            # Determinar el tipo de archivo según la extensión
            if extension == '.docx' or extension == '.doc':
                self.tipo = 'Word'
            elif extension == '.pdf':
                self.tipo = 'PDF'
            elif extension == '.xlsx' or extension == '.xls':
                self.tipo = 'Excel'
            elif extension in ['.jpg', '.jpeg', '.png', '.gif']:
                self.tipo = 'Imagen'
            elif extension == '.pptx' or extension == '.ppt':
                self.tipo = 'PowerPoint'
            else:
                self.tipo = 'Desconocido'  # Para tipos no reconocidos

            # Obtener el tamaño en KB
            self.tamaño = self.archivoss.size // 1024  # Convertir bytes a KB

        super().save(*args, **kwargs)


class Comentarios(models.Model):
    comentario = models.TextField()
    fecha_hora = models.DateTimeField(auto_now_add=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

