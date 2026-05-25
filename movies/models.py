from django.db import models

class Pelicula(models.Model):
    GENERO_SELECCIONABLES = [
        ('A', 'Accion'),
        ('H', 'Horror'),
        ('T', 'Thriller'),
        ('C', 'Comedia'),
    ]
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=30, choices=GENERO_SELECCIONABLES) 
    director = models.CharField(max_length=100)
    anio = models.DateField()
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='imagenes_peliculas/', null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.director}"