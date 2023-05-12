from django.shortcuts import render
from django.http import HttpResponse
from .models import Carrera
# Create your views here.

def home(request):
    return render(request,'core/home.html')
                #HttpResponse(
                        #"<h1>hola mundo, este es el home </h1>"+
                        #"<h4><a href=http://127.0.0.1:8000/carreras>ver carreras </a></h4>"+
                        #"<h4><a href=http://127.0.0.1:8000/docentes>ver docentes </a></h4>")

def docentes(request):
    return render(request,'core/docentes.html')
    #return HttpResponse("<h1>Docentes</h1>"+
                        #"<h4><a href=http://127.0.0.1:8000>volver a home </a></h4>"+
                        #"<h4><a href=http://127.0.0.1:8000/carreras>ver carreras </a></h4>")

def carreras(request):
    carreras = Carrera.objects.all()
    data = {
            'carreras':carreras
            }
    return render(request,'core/carreras.html', data)