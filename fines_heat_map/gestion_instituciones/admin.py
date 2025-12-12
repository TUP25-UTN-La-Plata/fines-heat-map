from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Partido, Localidad, SedeTipo, Sede
from .resources import PartidoResource, LocalidadResource, SedeTipoResource, SedeResource

# --- Mixin para manejo de Auditoría ---
class AuditAdminMixin:
    """Clase base para mostrar campos de auditoría como solo lectura"""
    readonly_fields = ('created_at', 'updated_at')
    
    def estado(self, obj):
        """Muestra un icono verde si está activo, rojo si tiene deleted_at"""
        if obj.deleted_at:
            return "❌ Eliminado"
        return "✅ Activo"
    estado.short_description = "Estado"

# --- Configuración de Modelos ---

@admin.register(Partido)
class PartidoAdmin(ImportExportModelAdmin, AuditAdminMixin):
    resource_class = PartidoResource
    list_display = ('nombre', 'estado', 'created_at')
    search_fields = ('nombre',)
    list_filter = ('created_at',)
    
    fieldsets = (
        ('Información', {'fields': ('nombre',)}),
        ('Auditoría', {'fields': ('created_at', 'updated_at', 'deleted_at'), 'classes': ('collapse',)}),
    )

@admin.register(Localidad)
class LocalidadAdmin(ImportExportModelAdmin, AuditAdminMixin):
    resource_class = LocalidadResource
    list_display = ('nombre', 'partido', 'codigo_postal', 'estado')
    search_fields = ('nombre', 'partido__nombre') # Necesario para autocomplete_fields en Sede
    list_filter = ('partido', 'created_at') # Ojo: si hay muchos partidos, esto puede ser lento
    autocomplete_fields = ['partido']
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Datos', {'fields': ('nombre', 'codigo_postal', 'partido')}),
        ('Auditoría', {'fields': ('created_at', 'updated_at', 'deleted_at'), 'classes': ('collapse',)}),
    )

@admin.register(SedeTipo)
class SedeTipoAdmin(ImportExportModelAdmin, AuditAdminMixin):
    resource_class = SedeTipoResource
    list_display = ('nombre', 'descripcion_corta', 'estado')
    search_fields = ('nombre',) # Necesario para autocomplete
    readonly_fields = ('created_at', 'updated_at')

    def descripcion_corta(self, obj):
        return (obj.descripcion[:50] + '...') if obj.descripcion and len(obj.descripcion) > 50 else obj.descripcion
    descripcion_corta.short_description = "Descripción"

    fieldsets = (
        (None, {'fields': ('nombre', 'descripcion')}),
        ('Auditoría', {'fields': ('created_at', 'updated_at', 'deleted_at'), 'classes': ('collapse',)}),
    )

@admin.register(Sede)
class SedeAdmin(ImportExportModelAdmin, AuditAdminMixin):
    resource_class = SedeResource
    # Columnas limpias para evitar el __str__ largo
    list_display = ('nombre', 'sede_tipo', 'localidad', 'direccion', 'estado')
    
    # Filtros laterales
    list_filter = ('sede_tipo', 'localidad__partido', 'created_at')
    
    # Buscador (permite buscar por nombre, dirección o nombre de localidad)
    search_fields = ('nombre', 'direccion', 'localidad__nombre')
    
    # Autocompletado: Vital para no cargar miles de localidades en un select
    autocomplete_fields = ['localidad', 'sede_tipo']
    
    # Campos de solo lectura
    readonly_fields = ('created_at', 'updated_at')

    # Organización visual del formulario
    fieldsets = (
        ('Datos Institucionales', {
            'fields': ('nombre', 'sede_tipo', 'telefono', 'email')
        }),
        ('Ubicación Geográfica', {
            'fields': ('direccion', 'localidad', 'lat', 'long'),
            'description': 'Coordenadas en formato decimal.'
        }),
        ('Información Adicional', {
            'fields': ('notas',),
            'classes': ('collapse',) # Oculto por defecto para limpiar visual
        }),
        ('Auditoría y Estado', {
            'fields': ('created_at', 'updated_at', 'deleted_at'),
            'classes': ('collapse',)
        }),
    )