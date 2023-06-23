from rest_framework import serializers
from core.models import Carrera

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'
        #flieds = ['nombre','duracion']
        #exclude = ['codigo'], se tiene que usa uno de los dos, no ambos