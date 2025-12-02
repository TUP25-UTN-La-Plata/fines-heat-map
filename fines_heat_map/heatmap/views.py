from django.shortcuts import render
from django.http import JsonResponse
from gestion_instituciones.models import Sede
from gestion_instituciones.serializers import SedeCompletaSerializer

def mapa(request):
    return render(request, "heatmap/mapa.html")


def get_sedes_data(request):
    # Endpoint para obtener los datos de las sedes con filtros de turno, orientación y módulo.
    sedes = (
        Sede.objects.filter(deleted_at=None)
        .select_related('localidad', 'localidad__partido', 'sede_tipo')
        .prefetch_related('comisiones', 'comisiones__orientacion', 'comisiones__modulo')
    )

    serializer = SedeCompletaSerializer(sedes, many=True)

    return JsonResponse(serializer.data, safe=False)