from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Carrera


def home(request):
    #return HttpResponse("<h1>Home</h1>")
    return render(request,'core/home.html')


def carreras(request):
    #obtener listado de carreras desde el Modelo
    carreras = Carrera.objects.all()

    #cargar listado en diccionario datos
    datos = {
        'carreras':carreras
    }
    #cargar diccionario datos en el request (Lo envía a template carreras.html)
    return render(request,'core/carreras.html',datos)

def nueva_carrera(request):
    if (request.POST):
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        duracion = int(request.POST['duracion'])

        #validaciones y lógica de negocio

        c = Carrera(codigo=codigo,nombre=nombre,duracion=duracion)
        c.save()
        
    
    #obtener listado de carreras desde el Modelo
    carreras = Carrera.objects.all()

    #cargar listado en diccionario datos
    datos = {
        'carreras':carreras
    }
    #cargar diccionario datos en el request (Lo envía a template carreras.html)
   
    return render(request,'core/nueva_carrera.html',datos)

def docentes(request):
    return render(request,'core/docentes.html')
