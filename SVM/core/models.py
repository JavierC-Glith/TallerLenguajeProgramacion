from django.db import models

class Habitacion(models.Model):
    numero = models.IntegerField(unique=True)
    ocupada = models.BooleanField(default=False)
    # Agrega otros campos según sea necesario

    def __str__(self):
        return str(self.numero)
