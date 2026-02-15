from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Orientacion, Modulo, Comision
from gestion_instituciones.models import Sede


class OrientacionResource(resources.ModelResource):
    class Meta:
        model = Orientacion
        fields = ('id', 'nombre', 'descripcion',)
        import_id_fields = ('nombre',)
        skip_unchanged = True
        report_skipped = True


class ModuloResource(resources.ModelResource):
    class Meta:
        model = Modulo
        fields = ('id', 'nombre', 'descripcion',)
        import_id_fields = ('nombre',)
        skip_unchanged = True
        report_skipped = True


class ComisionResource(resources.ModelResource):
    sede = fields.Field(
        column_name='sede_id',
        attribute='sede',
        widget=ForeignKeyWidget(Sede, 'nombre')  # Busca por nombre aunque la columna se llame sede_id
    )
    
    orientacion = fields.Field(
        column_name='orientacion_id',
        attribute='orientacion',
        widget=ForeignKeyWidget(Orientacion, 'id')
    )
    
    modulo = fields.Field(
        column_name='modulo_id',
        attribute='modulo',
        widget=ForeignKeyWidget(Modulo, 'id')
    )
    
    def skip_row(self, instance, original, row, import_validation_errors=None):
        """
        Salta filas vacías o que no tengan los campos requeridos.
        """
        # Verificar si la fila está vacía
        numero = str(row.get('numero', '')).strip() if row.get('numero') else ''
        sede_id = str(row.get('sede_id', '')).strip() if row.get('sede_id') else ''
        orientacion_id = str(row.get('orientacion_id', '')).strip() if row.get('orientacion_id') else ''
        modulo_id = str(row.get('modulo_id', '')).strip() if row.get('modulo_id') else ''
        turno = str(row.get('turno', '')).strip() if row.get('turno') else ''
        
        # Si todos los campos principales están vacíos, saltar la fila
        if not any([numero, sede_id, orientacion_id, modulo_id, turno]):
            return True
        
        # Si falta algún campo requerido (horario es opcional ahora), saltar la fila
        if not numero or not sede_id or not orientacion_id or not modulo_id or not turno:
            return True
        
        # Validar que el turno sea válido (incluye 'I' para Intermedio)
        if turno not in ['M', 'T', 'V', 'N', 'I']:
            return True
        
        return False
    
    class Meta:
        model = Comision
        fields = ('id', 'numero', 'sede', 'orientacion', 'modulo', 
                  'turno', 'horario', 'tutor', 'notas',)
        import_id_fields = ('numero',)
        skip_unchanged = True
        report_skipped = True
