from django.shortcuts import render


# def prueba(request):
#    return 10 / 0


def home(request):
    """Renderiza la pantalla principal con datos de ejemplo para desarrollo."""
    # Se mantienen datos mock para no depender de carga de BD en el home.
    places_example = [
        {
            "id": 1,
            "name": "Escuela Media N°3",
            "commission_number": "101",
            "city": "La Plata",
            "province": "Buenos Aires",
            "turno": "Noche",
            "address": "Av. 7 y 60",
            "lat": -34.9215,
            "lng": -57.9545,
        },
        {
            "id": 2,
            "name": "Centro Comunitario El Sol",
            "commission_number": "102",
            "city": "La Plata",
            "province": "Buenos Aires",
            "turno": "Tarde",
            "address": "Calle 12 y 50",
            "lat": -34.9105,
            "lng": -57.9435,
        },
    ]

    # `show_heatmap` arranca en False para evitar superposición inicial de capas.
    context = {"places": places_example, "show_heatmap": False}
    return render(request, "home.html", context)


def custom_404(request, exception):
    """Renderiza la página 404 personalizada."""
    return render(request, "404.html", status=404)


def custom_500(request):
    """Renderiza la página 500 personalizada."""
    return render(request, "500.html", status=500)


def preview_404(request):
    """Permite visualizar el template 404 en desarrollo."""
    return custom_404(request, exception=None)


def preview_500(request):
    """Permite visualizar el template 500 en desarrollo."""
    return custom_500(request)
