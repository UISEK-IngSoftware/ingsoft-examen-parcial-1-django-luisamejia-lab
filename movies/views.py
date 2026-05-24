from django.shortcuts import render 
from .models import Pelicula    

def lista_peliculas(request):
    peliculas = Pelicula.objects.all()  
    return render(request, 'movies/lista_peliculas.html', {'peliculas': peliculas}) 