from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CarreraSerializer
from core.models import Carrera

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class= CarreraSerializer

