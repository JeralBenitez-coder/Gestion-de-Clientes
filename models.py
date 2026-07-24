from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    edad = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nombre
     