from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

phone_validator = RegexValidator(regex=r'^\d{1,14}$', message="El número de teléfono solo puede contener hasta 14 dígitos.")

class User(AbstractUser):
    picture = models.ImageField(default='profile_default.png', upload_to='users/')
    location = models.CharField(max_length=60, default='No especificada')  
    number_phone = models.CharField(max_length=14, validators=[phone_validator], default='0000000000', blank=True)
