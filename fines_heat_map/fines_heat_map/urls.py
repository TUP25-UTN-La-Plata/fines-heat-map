"""
URL configuration for fines_heat_map project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import home, preview_404, preview_500

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    # Alias temporal para mantener compatibilidad con templates legacy.
    path("inicio/", home, name="map_home"),
    path("contacto/", TemplateView.as_view(template_name="contact.html"), name="contact"),
    path(
        "politica-privacidad/",
        TemplateView.as_view(template_name="privacy_policy.html"),
        name="privacy_policy",
    ),
    path(
        "politica-accesibilidad/",
        TemplateView.as_view(template_name="accessibility_policy.html"),
        name="accessibility_policy",
    ),
    # Vistas de previsualización para validar páginas de error en desarrollo.
    path("errores/404/", preview_404, name="preview_404"),
    path("errores/500/", preview_500, name="preview_500"),
    path(
        "mapa/",
        include(("heatmap.urls", "heatmap"), namespace="heatmap"),
    ),
    path(
        "instituciones/",
        include(
            ("gestion_instituciones.urls", "gestion_instituciones"),
            namespace="instituciones",
        ),
    ),
    path(
        "comisiones/",
        include(
            ("gestion_comisiones.urls", "gestion_comisiones"),
            namespace="comisiones",
        ),
    ),
]

handler404 = "fines_heat_map.views.custom_404"
handler500 = "fines_heat_map.views.custom_500"
