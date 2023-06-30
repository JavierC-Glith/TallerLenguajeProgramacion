from django.shortcuts import render
from .models import Habitacion

def habitaciones_disponibles(request):
    habitaciones = Habitacion.objects.filter(ocupada=False)
    cantidad = habitaciones.count()
    return render(request, 'core/disponibles.html', {'habitaciones': habitaciones, 'cantidad':cantidad})

def habitaciones_ocupadas(request):
    habitaciones = Habitacion.objects.filter(ocupada=True)
    return render(request, 'core/ocupadas.html', {'habitaciones': habitaciones})

