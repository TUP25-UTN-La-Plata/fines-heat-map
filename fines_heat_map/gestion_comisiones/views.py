from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Modulo, Orientacion
from .serializers import ModuloSerializer, OrientacionSerializer


# Create your views here.
def comisiones(request):
    return render(request, "gestion_comisiones/comisiones.html")


@api_view(['GET'])
def get_all_modulos(request):
    """
    API endpoint para obtener todos los módulos activos.
    GET /comisiones/api/modulos/
    """
    modulos = Modulo.objects.filter(deleted_at=None).order_by('nombre')
    serializer = ModuloSerializer(modulos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_orientaciones(request):
    """
    API endpoint para obtener todas las orientaciones activas.
    GET /comisiones/api/orientaciones/
    """
    orientaciones = Orientacion.objects.filter(deleted_at=None).order_by('nombre')
    serializer = OrientacionSerializer(orientaciones, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
