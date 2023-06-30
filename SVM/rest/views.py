from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HabitacionSerializer
from core.models import Habitacion

class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class= HabitacionSerializer