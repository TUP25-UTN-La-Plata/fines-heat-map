from django.shortcuts import render
from django.core.paginator import Paginator

# ====== DATOS DE PRUEBA - ACTIVAR/DESACTIVAR AQUÍ ======
USE_TEST_DATA = True  # Cambiar a False para volver al estado original


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
            "orientation": "Técnica",
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
    ]


# Create your views here.
def lista_instituciones(request):
    if USE_TEST_DATA:
        # Simular paginación con datos de prueba
        test_places = get_test_data()
        paginator = Paginator(test_places, 10)  # 10 por página
        page = request.GET.get("page", 1)
        paginated_places = paginator.get_page(page)

        context = {"paginator": paginated_places}
    else:
        context = {}

    return render(request, "gestion_instituciones/place_list.html", context)
