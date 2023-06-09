from django.db import models
from .choices import niveles
# Create your models here.

class Categoria(models.Model):
    nombre = models.TextField(verbose_name="Nombre")
    descripcion = models.TextField(verbose_name="Descripcion")

    def __str__(self):
        return f"{self.nombre} ({self.descripcion})"
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'

class Comunicado(models.Model):
    titulo = models.TextField()
    detalle = models.TextField()
    fecha_envio = models.DateTimeField()
    fecha_ultima_modificacion = models.DateTimeField()
    nivel = models.CharField(max_length=20 ,choices=niveles, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
    autor = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return f"{self.titulo} {self.categoria} {self.nivel} {self.autor}"
    
    class Meta:
        ordering = ['-fecha_envio']
    
     
