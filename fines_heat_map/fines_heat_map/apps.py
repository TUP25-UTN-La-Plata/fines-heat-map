from django.apps import AppConfig


class FinesHeatMapConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fines_heat_map'
    verbose_name = 'FinEs Heat Map'

    def ready(self):
        # Importar aquí para evitar importaciones circulares
        from . import admin_init  # noqa

