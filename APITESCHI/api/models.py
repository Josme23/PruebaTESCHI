from django.db import models

# Create your models here.

class dispositivo(models.Model):
    nombre_del_dispositivo = models.CharField(max_length=100)
    quien_realiza = models.DecimalField(max_length=100)
    descripcion = models.TextField()

        