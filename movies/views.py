from django.shortcuts import render 
from .models import Pelicula  
from django.template import loader
from django.http import HttpResponse 
from .models import Pelicula

def index(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'index.html', {'peliculas': peliculas})

def detalle_pelicula(request, pelicula_id):
    pelicula = Pelicula.objects.get(id=pelicula_id)
    template = loader.get_template('detalle_pelicula.html')
    context = {
        'pelicula': pelicula
    }
    return render(request, 'detalle_pelicula.html', {'pelicula': pelicula})
