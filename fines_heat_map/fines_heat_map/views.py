from django.shortcuts import render


# def prueba(request):
#    return 10 / 0


def home(request):
    # Datos de ejemplo para mostrar en el sidebar
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

    context = {"places": places_example, "show_heatmap": False}
    return render(request, "home.html", context)
