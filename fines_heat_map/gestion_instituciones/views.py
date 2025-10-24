from django.shortcuts import render


# Create your views here.
def instituciones(request):
    return render(request, "gestion_instituciones/instituciones.html")  # ← Cambiar esto
