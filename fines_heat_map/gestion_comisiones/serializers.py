from rest_framework import serializers
from .models import Modulo, Orientacion


class ModuloSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Modulo"""
    
    class Meta:
        model = Modulo
        fields = ['id', 'nombre', 'descripcion']


class OrientacionSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Orientacion"""
    
    class Meta:
        model = Orientacion
        fields = ['id', 'nombre', 'descripcion']

