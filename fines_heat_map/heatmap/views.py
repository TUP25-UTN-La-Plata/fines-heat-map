from django.db.models import Q
from django.shortcuts import render
from django.conf import settings
from .forms import MapFilterForm
from django.http import JsonResponse
from gestion_instituciones.models import Sede
from gestion_instituciones.serializers import SedeCompletaSerializer

def mapa(request):
    """
    Vista del mapa interactivo con filtros dinámicos.
    """
    # Inicializar formulario con datos GET
    form = MapFilterForm(request.GET or None)

    # Obtener parámetros para centrar el mapa en una ubicación específica
    center_lat = request.GET.get("lat")
    center_lng = request.GET.get("lng")
    zoom_level = request.GET.get("zoom", str(settings.MAP_CONFIG["default_zoom"]))
    place_name = request.GET.get("name")
    show_heatmap = request.GET.get("heatmap", "").lower() == "true"

    # Obtener datos de lugares (usar ejemplo de settings por ahora)
    places_data = settings.EXAMPLE_PLACES.copy()

    # Aplicar filtros si el formulario es válido
    if form.is_valid():
        filters = form.get_filter_params()

        if filters.get("search"):
            search_term = filters["search"].lower()
            places_data = [
                place for place in places_data if search_term in place["name"].lower()
            ]

        if filters.get("province"):
            places_data = [
                place
                for place in places_data
                if place["province"] == filters["province"]
            ]

        if filters.get("city"):
            places_data = [
                place for place in places_data if place["city"] == filters["city"]
            ]

        if filters.get("turno"):
            places_data = [
                place
                for place in places_data
                if place["turno"].lower() == filters["turno"].lower()
            ]

        if filters.get("modules"):
            places_data = [
                place
                for place in places_data
                if filters["modules"] in place.get("modules", [])
            ]

        if filters.get("orientation"):
            places_data = [
                place
                for place in places_data
                if place.get("orientation") == filters["orientation"]
            ]

    # TODO: Reemplazar con consulta real a modelos cuando estén listos
    # from .models import Place
    # places = Place.objects.filter(**filters)
    # places_data = [place.to_dict() for place in places]

    context = {
        "form": form,
        "places": places_data,
        "center_lat": center_lat,
        "center_lng": center_lng,
        "zoom_level": zoom_level,
        "place_name": place_name,
        "show_heatmap": show_heatmap,
        "map_config": settings.MAP_CONFIG,
    }
    return render(request, "home.html", context)


def get_sedes_data(request):
    # Endpoint para obtener los datos de las sedes con filtros de turno, orientación y módulo.

     # Obtener parámetros de query (solo IDs y letra de turno)
    modulo_id = request.GET.get('moduloID')
    turno = request.GET.get('turno')  # 'M', 'T', 'V', 'N'
    orientacion_id = request.GET.get('orientacionID')

    sedes = (
        Sede.objects.filter(deleted_at=None)
        .select_related('localidad', 'localidad__partido', 'sede_tipo')
        .prefetch_related('comisiones', 'comisiones__orientacion', 'comisiones__modulo')
    )

    # Aplicar filtros solo si hay parámetros
    # Si alguna comisión de la sede cumple los criterios, traemos la sede completa
    if modulo_id or turno or orientacion_id:
        filters = Q(comisiones__deleted_at=None)  # Solo comisiones activas
        
        if modulo_id:
            try:
                filters &= Q(comisiones__modulo_id=int(modulo_id))
            except (ValueError, TypeError):
                pass
        
        if turno:
            # Validar que sea una letra válida
            if turno in ['M', 'T', 'V', 'N']:
                filters &= Q(comisiones__turno=turno)
        
        if orientacion_id:
            try:
                filters &= Q(comisiones__orientacion_id=int(orientacion_id))
            except (ValueError, TypeError):
                pass
        
        # Filtrar sedes que tengan al menos una comisión que cumpla los criterios
        sedes = sedes.filter(filters).distinct()

    serializer = SedeCompletaSerializer(sedes, many=True)

    return JsonResponse(serializer.data, safe=False)


def buscar_sedes_por_nombre(request):
    # Endpoint para buscar sedes por nombre (búsqueda parcial, case-insensitive)
    nombre = request.GET.get('nombre', '').strip()
    
    if not nombre:
        return JsonResponse({'error': 'El parámetro "nombre" es requerido'}, status=400)
    
    # Búsqueda case-insensitive que contiene el término
    sedes = (
        Sede.objects.filter(
            deleted_at=None,
            nombre__icontains=nombre
        )
        .select_related('localidad', 'localidad__partido', 'sede_tipo')
        .prefetch_related('comisiones', 'comisiones__orientacion', 'comisiones__modulo')
    )
    
    serializer = SedeCompletaSerializer(sedes, many=True)
    
    return JsonResponse(serializer.data, safe=False)
