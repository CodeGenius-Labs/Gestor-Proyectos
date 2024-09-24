from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

phone_validator = RegexValidator(regex=r'^\d{1,14}$', message="El número de teléfono solo puede contener hasta 14 dígitos.")

class User(AbstractUser):
    picture = models.ImageField(default='profile_default.png', upload_to='users/')
    location = models.CharField(max_length=60, default='No especificada')  
    number_phone = models.CharField(max_length=14, validators=[phone_validator], default='0000000000', blank=True)

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
    SUPERADMIN = 'Superadmin'

    ROLE_CHOICES = [
        (ADMIN_DEPARTAMENTO, 'Administrador del departamento'),
        (TUTOR, 'Tutor'),
        (ASISTENTE, 'Asistente'),
        (SUPERADMIN, 'Superadmin'),
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
    archivoss = models.FileField(upload_to='archivos/', default='archivos/prueba.txt')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


class Comentarios(models.Model):
    comentario = models.TextField()
    fecha_hora = models.DateTimeField(null=True, blank=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
