# ARCHIVO DE RESPALDO - CONTENIDO ORIGINAL DE views.py
# Para revertir, copiar este contenido a gestion_instituciones/views.py

from django.shortcuts import render


# Create your views here.
def lista_instituciones(request):
    return render(request, "gestion_instituciones/place_list.html")


def detalle_institucion(request, pk):
    # Lógica para obtener los detalles de la institución con el id `pk`
    return render(request, "gestion_instituciones/place_detail.html")
