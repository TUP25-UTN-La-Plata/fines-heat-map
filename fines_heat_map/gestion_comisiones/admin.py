from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Orientacion, Modulo, Comision
from .resources import OrientacionResource, ModuloResource, ComisionResource

# Reutilizamos el Mixin de auditoría (copialo aquí para no complicar imports entre apps)
class AuditAdminMixin:
    readonly_fields = ('created_at', 'updated_at')
    
    def estado(self, obj):
        if obj.deleted_at:
            return "❌ Eliminado"
        return "✅ Activo"
    estado.short_description = "Estado"

@admin.register(Orientacion)
class OrientacionAdmin(ImportExportModelAdmin, AuditAdminMixin):
    resource_class = OrientacionResource
    list_display = ('nombre', 'descripcion', 'estado')
    search_fields = ('nombre',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('nombre', 'descripcion')}),
        ('Auditoría', {'fields': ('created_at', 'updated_at', 'deleted_at'), 'classes': ('collapse',)}),
    )

@admin.register(Modulo)
class ModuloAdmin(ImportExportModelAdmin, AuditAdminMixin):
    resource_class = ModuloResource
    list_display = ('nombre', 'descripcion', 'estado')
    search_fields = ('nombre',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('nombre', 'descripcion')}),
        ('Auditoría', {'fields': ('created_at', 'updated_at', 'deleted_at'), 'classes': ('collapse',)}),
    )

@admin.register(Comision)
class ComisionAdmin(ImportExportModelAdmin, AuditAdminMixin):
    resource_class = ComisionResource
    list_display = ('numero', 'sede', 'orientacion', 'modulo', 'turno', 'estado')
    list_filter = ('turno', 'modulo', 'orientacion', 'sede__localidad__partido')
    search_fields = ('numero', 'sede__nombre', 'tutor')
    readonly_fields = ('created_at', 'updated_at')
    
    # ¡IMPORTANTE! Esto activa el buscador de sedes dentro de la comisión
    autocomplete_fields = ['sede', 'orientacion', 'modulo'] 
    
    fieldsets = (
        ('Datos Académicos', {
            'fields': ('numero', 'sede', 'orientacion', 'modulo', 'turno')
        }),
        ('Detalles', {
            'fields': ('horario', 'tutor', 'notas')
        }),
        ('Auditoría', {
            'fields': ('created_at', 'updated_at', 'deleted_at'), 
            'classes': ('collapse',)
        }),
    )