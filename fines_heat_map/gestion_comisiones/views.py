from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Modulo, Orientacion
from .serializers import ModuloSerializer, OrientacionSerializer


# Create your views here.
def comisiones(request):
    """Renderiza la pantalla principal del módulo de comisiones."""
    return render(request, "gestion_comisiones/comisiones.html")


@api_view(['GET'])
def get_all_modulos(request):
    """
    API endpoint para obtener todos los módulos activos.
    GET /comisiones/api/modulos/
    """
    # Solo se exponen módulos activos para poblar filtros del frontend.
    modulos = Modulo.objects.filter(deleted_at=None).order_by('nombre')
    serializer = ModuloSerializer(modulos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_orientaciones(request):
    """
    API endpoint para obtener todas las orientaciones activas.
    GET /comisiones/api/orientaciones/
    """
    # Solo se exponen orientaciones activas para poblar filtros del frontend.
    orientaciones = Orientacion.objects.filter(deleted_at=None).order_by('nombre')
    serializer = OrientacionSerializer(orientaciones, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
