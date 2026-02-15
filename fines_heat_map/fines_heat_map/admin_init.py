"""
Inicialización personalizada del admin.
Agrega la URL del dashboard al admin site.
"""
from django.contrib import admin
from django.urls import path
from .admin_views import dashboard_view

# Guardar el método get_urls original
_original_get_urls = admin.site.get_urls

def custom_get_urls():
    """
    Agrega la URL del dashboard al admin site.
    """
    urls = _original_get_urls()
    # Insertar la URL del dashboard antes de las URLs del admin
    urls.insert(0, path('dashboard/', dashboard_view, name='dashboard'))
    return urls

# Sobrescribir get_urls del admin site
admin.site.get_urls = custom_get_urls

