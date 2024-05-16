from typing import Any
from django.db import models

# Create your models here.
class Libro(models.Model):
    idlibro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='imagenes/libros/', verbose_name='Imagen', null=True)
    descripcion = models.TextField(verbose_name='Descripción', null=True)
    cantidad = models.IntegerField()
    precio = models.FloatField()

    def __str__(self):
        return f"Título: {self.titulo} - Descripción: {self.descripcion}"
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()