from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import InstitucionFilterForm

# ====== DATOS DE PRUEBA - ACTIVAR/DESACTIVAR AQUÍ ======
USE_TEST_DATA = False  # Cambiar a False para volver al estado original


def get_test_data():
    """Datos simulados para testing - TEMPORAL"""
    if not USE_TEST_DATA:
        return []

    return [
        {
            "id": 1,
            "name": "Escuela Secundaria N° 15",
            "commission_number": "1A",
            "tutor_name": "María González",
            "turno": "Mañana",
            "modules": ["Matemática", "Lengua", "Historia"],
            "orientation": "Ciencias Sociales",
            "address": "Av. 7 N° 1234",
            "city": "La Plata",
            "province": "Buenos Aires",
            "postal_code": "B1900",
            "lat": -34.9215,
            "lng": -57.9545,
            "phone": "221-555-0101",
            "email": "escuela15@abc.gob.ar",
            "website": "https://escuela15.edu.ar",
            "schedule": "Lunes a Viernes de 8:00 a 12:00",
            "offers_online": True,
            "summary": "Institución educativa con amplia trayectoria en educación de adultos.",
        },
        {
            "id": 2,
            "name": "Centro Educativo Municipal",
            "commission_number": "2B",
            "tutor_name": "Carlos Rodríguez",
            "turno": "Tarde",
            "modules": ["Biología", "Química", "Física"],
            "orientation": "Ciencias Naturales",
            "address": "Calle 50 N° 789",
            "city": "Berisso",
            "province": "Buenos Aires",
            "postal_code": "B1923",
            "lat": -34.8719,
            "lng": -57.8828,
            "phone": "221-555-0202",
            "email": "centro.berisso@municipio.gob.ar",
            "website": "",
            "schedule": "Lunes a Viernes de 14:00 a 18:00",
            "offers_online": False,
            "summary": "Centro municipal enfocado en ciencias naturales y experimentación.",
        },
        {
            "id": 3,
            "name": "Instituto Técnico Industrial",
            "commission_number": "3C",
            "tutor_name": "Ana Martínez",
            "turno": "Noche",
            "modules": ["Tecnología", "Electricidad", "Mecánica"],
            "orientation": "Economía y Administración",
            "address": "Ruta 11 Km 15",
            "city": "Ensenada",
            "province": "Buenos Aires",
            "postal_code": "B1925",
            "lat": -34.8569,
            "lng": -57.9067,
            "phone": "221-555-0303",
            "email": "tecnico.ensenada@instituto.edu.ar",
            "website": "https://tecnico-ensenada.edu.ar",
            "schedule": "Lunes a Viernes de 18:00 a 22:00",
            "offers_online": True,
            "summary": "Formación técnica especializada para el sector industrial.",
        },
        {
            "id": 4,
            "name": "Escuela de Arte y Comunicación",
            "commission_number": "4D",
            "tutor_name": "Laura Fernández",
            "turno": "Tarde",
            "modules": ["Plástica", "Música", "Teatro"],
            "orientation": "Arte",
            "address": "Diagonal 74 N° 456",
            "city": "La Plata",
            "province": "Buenos Aires",
            "postal_code": "B1904",
            "lat": -34.9014,
            "lng": -57.9544,
            "phone": "221-555-0404",
            "email": "arte.laplata@escuela.edu.ar",
            "website": "https://arte-laplata.edu.ar",
            "schedule": "Lunes a Viernes de 13:00 a 17:00",
            "offers_online": False,
            "summary": "Formación artística integral con enfoque en expresión creativa.",
        },
        {
            "id": 5,
            "name": "Centro Educativo Rosario Norte",
            "commission_number": "5E",
            "tutor_name": "Roberto Silva",
            "turno": "Mañana",
            "modules": ["Economía", "Administración", "Contabilidad"],
            "orientation": "Economía y Administración",
            "address": "Av. Pellegrini 1500",
            "city": "Rosario",
            "province": "Santa Fe",
            "postal_code": "S2000",
            "lat": -32.9468,
            "lng": -60.6393,
            "phone": "341-555-0505",
            "email": "rosario.norte@centro.edu.ar",
            "website": "https://rosario-norte.edu.ar",
            "schedule": "Lunes a Viernes de 8:00 a 12:00",
            "offers_online": True,
            "summary": "Especialización en administración y gestión empresarial.",
        },
        {
            "id": 6,
            "name": "Instituto Comunicación Social",
            "commission_number": "6F",
            "tutor_name": "Patricia López",
            "turno": "Noche",
            "modules": ["Periodismo", "Medios", "Comunicación"],
            "orientation": "Comunicación",
            "address": "Calle 13 N° 890",
            "city": "Berisso",
            "province": "Buenos Aires",
            "postal_code": "B1923",
            "lat": -34.8619,
            "lng": -57.8728,
            "phone": "221-555-0606",
            "email": "comunicacion@instituto.edu.ar",
            "website": "",
            "schedule": "Lunes a Viernes de 19:00 a 23:00",
            "offers_online": True,
            "summary": "Formación en comunicación social y medios digitales.",
        },
    ]


# Create your views here.
def lista_instituciones(request):
    # Inicializar formulario con datos GET
    form = InstitucionFilterForm(request.GET or None)
    
    if USE_TEST_DATA:
        # Obtener datos de prueba
        test_places = get_test_data()
        
        # Aplicar filtros si el formulario es válido
        if form.is_valid():
            filters = form.get_filter_params()
            
            # Filtro por búsqueda de nombre
            if filters.get('search'):
                search_term = filters['search'].lower()
                test_places = [
                    place for place in test_places 
                    if search_term in place['name'].lower()
                ]
            
            # Filtro por provincia
            if filters.get('province'):
                test_places = [
                    place for place in test_places 
                    if place['province'] == filters['province']
                ]
            
            # Filtro por ciudad
            if filters.get('city'):
                city_term = filters['city'].lower()
                test_places = [
                    place for place in test_places 
                    if city_term in place['city'].lower()
                ]
            
            # Filtro por turno
            if filters.get('turno'):
                test_places = [
                    place for place in test_places 
                    if place['turno'] == filters['turno']
                ]
            
            # Filtro por orientación
            if filters.get('orientation'):
                test_places = [
                    place for place in test_places 
                    if place.get('orientation') == filters['orientation']
                ]
        
        # Simular paginación con datos filtrados
        paginator = Paginator(test_places, 10)  # 10 por página
        page = request.GET.get("page", 1)
        paginated_places = paginator.get_page(page)

        context = {
            "form": form,
            "paginator": paginated_places,
            "total_results": len(test_places)
        }
    else:
        context = {"form": form}

    return render(request, "gestion_instituciones/place_list.html", context)


def detalle_institucion(request, pk):
    """Vista de detalle de una institución"""
    if USE_TEST_DATA:
        # Buscar en datos de prueba
        test_places = get_test_data()
        place = next((p for p in test_places if p['id'] == int(pk)), None)
        
        if not place:
            from django.http import Http404
            raise Http404("Institución no encontrada")
        
        context = {"place": place}
    else:
        # Cuando tengamos modelos reales
        from django.shortcuts import get_object_404
        from .models import Sede
        place = get_object_404(Sede, pk=pk, deleted_at=None)
        context = {"place": place}
    
    return render(request, "gestion_instituciones/place_detail.html", context)
