from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Partido, Localidad, SedeTipo, Sede


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
    sede_tipo = fields.Field(
        column_name='sede_tipo',
        attribute='sede_tipo',
        widget=ForeignKeyWidget(SedeTipo, 'nombre')
    )
    
    localidad = fields.Field(
        column_name='localidad',
        attribute='localidad',
        widget=ForeignKeyWidget(Localidad, 'nombre')
    )
    
    def skip_row(self, instance, original, row, import_validation_errors=None):
        """
        Salta filas vacías o que no tengan los campos requeridos.
        """
        # Verificar si la fila está vacía (todos los campos principales están vacíos)
        nombre = str(row.get('nombre', '')).strip() if row.get('nombre') else ''
        sede_tipo = str(row.get('sede_tipo', '')).strip() if row.get('sede_tipo') else ''
        direccion = str(row.get('direccion', '')).strip() if row.get('direccion') else ''
        localidad = str(row.get('localidad', '')).strip() if row.get('localidad') else ''
        lat = str(row.get('lat', '')).strip() if row.get('lat') else ''
        long = str(row.get('long', '')).strip() if row.get('long') else ''
        
        # Si todos los campos principales están vacíos, saltar la fila
        if not any([nombre, sede_tipo, direccion, localidad, lat, long]):
            return True
        
        # Si falta algún campo requerido, saltar la fila
        if not nombre or not sede_tipo or not direccion or not localidad or not lat or not long:
            return True
        
        return False
    
    class Meta:
        model = Sede
        fields = ('id', 'nombre', 'sede_tipo', 'direccion', 'localidad', 
                'telefono', 'email', 'lat', 'long', 'notas',)
        import_id_fields = ('nombre',)
        skip_unchanged = True
        report_skipped = True
