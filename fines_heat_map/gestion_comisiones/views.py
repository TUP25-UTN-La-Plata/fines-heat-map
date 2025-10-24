from django.shortcuts import render


# Create your views here.
def comisiones(request):
    return render(request, "gestion_comisiones/comisiones.html")  # ← Cambiar esto
