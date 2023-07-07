from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HabitacionSerializer
from core.models import Habitacion
from django.http import JsonResponse

class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.filter(ocupada=False)
    serializer_class= HabitacionSerializer


