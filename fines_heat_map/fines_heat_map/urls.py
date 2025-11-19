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
from .views import home


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
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
