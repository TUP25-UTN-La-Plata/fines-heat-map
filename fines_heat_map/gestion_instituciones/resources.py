from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Partido, Localidad, SedeTipo, Sede


class FlexibleForeignKeyWidget(ForeignKeyWidget):
    """
    Widget que acepta tanto ID como nombre para ForeignKey.
    Intenta primero por ID, luego por nombre.
    También puede leer de columnas alternativas (ej: sede_tipo_id o localidad_id).
    Prioriza la columna alternativa si existe.
    """
    def __init__(self, model, field='id', alt_column_name=None):
        super().__init__(model, field)
        self.alt_column_name = alt_column_name
    
    def clean(self, value, row=None, **kwargs):
        # Priorizar la columna alternativa si existe
        if self.alt_column_name and row:
            alt_value = row.get(self.alt_column_name)
            if alt_value and str(alt_value).strip():
                value = alt_value
        
        # Si no hay valor en ninguna columna, retornar None
        if not value or not str(value).strip():
            return None
        
        # Intentar primero por ID
        try:
            int_value = int(value)
            return self.model.objects.get(id=int_value)
        except (ValueError, TypeError, self.model.DoesNotExist):
            pass
        
        # Si no funciona, intentar por nombre (comportamiento original)
        return super().clean(value, row, **kwargs)


class PartidoResource(resources.ModelResource):
    class Meta:
        model = Partido
        fields = ('id', 'nombre',)
        import_id_fields = ('nombre',)  # Usa 'nombre' como identificador único
        skip_unchanged = True
        report_skipped = True


class LocalidadResource(resources.ModelResource):
    partido = fields.Field(
        column_name='partido',
        attribute='partido',
        widget=ForeignKeyWidget(Partido, 'nombre')
    )
    
    class Meta:
        model = Localidad
        fields = ('id', 'nombre', 'partido', 'codigo_postal',)
        import_id_fields = ('nombre', 'partido',)  # Identificador compuesto
        skip_unchanged = True
        report_skipped = True


class SedeTipoResource(resources.ModelResource):
    class Meta:
        model = SedeTipo
        fields = ('id', 'nombre', 'descripcion',)
        import_id_fields = ('nombre',)
        skip_unchanged = True
        report_skipped = True


class SedeResource(resources.ModelResource):
    # Campo sede_tipo que lee directamente de 'sede_tipo_id'
    sede_tipo = fields.Field(
        column_name='sede_tipo_id',
        attribute='sede_tipo',
        widget=ForeignKeyWidget(SedeTipo, 'id'),
        saves_null_values=False
    )
    
    # Campo localidad que lee directamente de 'localidad_id'
    localidad = fields.Field(
        column_name='localidad_id',
        attribute='localidad',
        widget=ForeignKeyWidget(Localidad, 'id'),
        saves_null_values=False
    )
    
    def skip_row(self, instance, original, row, import_validation_errors=None):
        """
        Salta filas vacías o que no tengan los campos requeridos.
        """
        # Verificar si la fila está vacía (todos los campos principales están vacíos)
        nombre = str(row.get('nombre', '')).strip() if row.get('nombre') else ''
        sede_tipo_id = str(row.get('sede_tipo_id', '')).strip() if row.get('sede_tipo_id') else ''
        direccion = str(row.get('direccion', '')).strip() if row.get('direccion') else ''
        localidad_id = str(row.get('localidad_id', '')).strip() if row.get('localidad_id') else ''
        lat = str(row.get('lat', '')).strip() if row.get('lat') else ''
        long = str(row.get('long', '')).strip() if row.get('long') else ''
        
        # Si todos los campos principales están vacíos, saltar la fila
        if not any([nombre, sede_tipo_id, direccion, localidad_id, lat, long]):
            return True
        
        # Si falta algún campo requerido, saltar la fila
        if not nombre or not sede_tipo_id or not direccion or not localidad_id or not lat or not long:
            return True
        
        return False
    
    class Meta:
        model = Sede
        fields = ('id', 'nombre', 'sede_tipo', 'direccion', 
                'localidad', 'telefono', 'email', 'lat', 'long', 'notas',)
        import_id_fields = ('nombre',)
        skip_unchanged = True
        report_skipped = True
        # Mapeo de columnas: los campos 'sede_tipo' y 'localidad' leen de 'sede_tipo_id' y 'localidad_id'
        # Esto se define en los fields.Field arriba con column_name
