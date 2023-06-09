from django.shortcuts import render
from .models import Comunicado
from .models import Categoria
# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def comunicados(request):
    datos = Comunicado.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'core/comunicados.html', {'datos': datos})

def buscar(request):
    buscar= request.GET["encontrar"]
    datos = Comunicado.objects.filter(titulo__icontains=buscar)
    return render(request, 'core/comunicados.html', {'datos': datos})

       




