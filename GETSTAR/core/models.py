from django.db import models

# Create your models here.
class Comunicado(models.Model):
    titulo = models.TextField()
    detalle = models.TextField()
    fecha_envio = models.DateTimeField()
    fecha_ultima_modificacion = models.DateTimeField()

class Categoria(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()