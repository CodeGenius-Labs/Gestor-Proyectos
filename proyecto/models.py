from django.db import models
from user.models import User

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


class Comentarios(models.Model):
    comentario = models.TextField()
    fecha_hora = models.DateTimeField(auto_now_add=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

