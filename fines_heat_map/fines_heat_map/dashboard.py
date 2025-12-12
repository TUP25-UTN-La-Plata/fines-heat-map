from django.db.models import Count, Q
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
import json
from gestion_instituciones.models import Sede, Partido, Localidad
from gestion_comisiones.models import Comision, Orientacion, Modulo


def dashboard_callback(request, *args, **kwargs):
    """
    Callback para el dashboard de unfold con estadísticas y gráficos.
    Acepta argumentos adicionales para compatibilidad con unfold.
    """
    # Estadísticas generales
    total_sedes = Sede.objects.filter(deleted_at=None).count()
    total_comisiones = Comision.objects.filter(deleted_at=None).count()
    
    # Comisiones por turno
    comisiones_por_turno = Comision.objects.filter(deleted_at=None).values('turno').annotate(
        cantidad=Count('id')
    ).order_by('turno')
    
    turno_labels = []
    turno_data = []
    turno_colors_map = {
        'M': '#3B82F6',  # Azul para Mañana
        'T': '#10B981',  # Verde para Tarde
        'V': '#F59E0B',  # Amarillo para Vespertino
        'N': '#8B5CF6',  # Púrpura para Noche
    }
    
    turno_nombres = {
        'M': 'Mañana',
        'T': 'Tarde',
        'V': 'Vespertino',
        'N': 'Noche',
    }
    
    turno_colors = []
    for item in comisiones_por_turno:
        turno_labels.append(turno_nombres.get(item['turno'], item['turno']))
        turno_data.append(item['cantidad'])
        turno_colors.append(turno_colors_map.get(item['turno'], '#6B7280'))
    
    # Comisiones por orientación
    comisiones_por_orientacion = Comision.objects.filter(deleted_at=None).values(
        'orientacion__nombre'
    ).annotate(cantidad=Count('id')).order_by('-cantidad')[:10]
    
    orientacion_labels = [item['orientacion__nombre'] for item in comisiones_por_orientacion]
    orientacion_data = [item['cantidad'] for item in comisiones_por_orientacion]
    
    # Comisiones por módulo
    comisiones_por_modulo = Comision.objects.filter(deleted_at=None).values(
        'modulo__nombre'
    ).annotate(cantidad=Count('id')).order_by('-cantidad')[:10]
    
    modulo_labels = [item['modulo__nombre'] for item in comisiones_por_modulo]
    modulo_data = [item['cantidad'] for item in comisiones_por_modulo]
    
    # Comisiones por partido
    comisiones_por_partido = Comision.objects.filter(
        deleted_at=None,
        sede__localidad__partido__deleted_at=None
    ).values(
        'sede__localidad__partido__nombre'
    ).annotate(cantidad=Count('id')).order_by('-cantidad')[:10]
    
    partido_labels = [item['sede__localidad__partido__nombre'] for item in comisiones_por_partido]
    partido_data = [item['cantidad'] for item in comisiones_por_partido]
    
    # Comisiones por localidad
    comisiones_por_localidad = Comision.objects.filter(
        deleted_at=None,
        sede__localidad__deleted_at=None
    ).values(
        'sede__localidad__nombre'
    ).annotate(cantidad=Count('id')).order_by('-cantidad')[:10]
    
    localidad_labels = [item['sede__localidad__nombre'] for item in comisiones_por_localidad]
    localidad_data = [item['cantidad'] for item in comisiones_por_localidad]
    
    # Retornar datos con JSON seguro para el template
    return {
        "total_sedes": total_sedes,
        "total_comisiones": total_comisiones,
        "turno_labels": mark_safe(json.dumps(turno_labels)),
        "turno_data": mark_safe(json.dumps(turno_data)),
        "turno_colors": mark_safe(json.dumps(turno_colors)),
        "orientacion_labels": mark_safe(json.dumps(orientacion_labels)),
        "orientacion_data": mark_safe(json.dumps(orientacion_data)),
        "modulo_labels": mark_safe(json.dumps(modulo_labels)),
        "modulo_data": mark_safe(json.dumps(modulo_data)),
        "partido_labels": mark_safe(json.dumps(partido_labels)),
        "partido_data": mark_safe(json.dumps(partido_data)),
        "localidad_labels": mark_safe(json.dumps(localidad_labels)),
        "localidad_data": mark_safe(json.dumps(localidad_data)),
    }

