from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nombre
class Equipos (models.Model):
    Equipo = models.CharField(max_length=100)
    Numero_de_serie = models.IntegerField()

class Detalles (models.Model):
    Estado_antes_de = models.CharField(max_length=100)
    Estado_actual = models.CharField(max_length=100)

            