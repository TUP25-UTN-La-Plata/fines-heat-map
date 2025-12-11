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
        column_name='sede',
        attribute='sede',
        widget=ForeignKeyWidget(Sede, 'nombre')
    )
    
    orientacion = fields.Field(
        column_name='orientacion',
        attribute='orientacion',
        widget=ForeignKeyWidget(Orientacion, 'nombre')
    )
    
    modulo = fields.Field(
        column_name='modulo',
        attribute='modulo',
        widget=ForeignKeyWidget(Modulo, 'nombre')
    )
    
    def skip_row(self, instance, original, row, import_validation_errors=None):
        """
        Salta filas vacías o que no tengan los campos requeridos.
        """
        # Verificar si la fila está vacía
        numero = str(row.get('numero', '')).strip() if row.get('numero') else ''
        sede = str(row.get('sede', '')).strip() if row.get('sede') else ''
        orientacion = str(row.get('orientacion', '')).strip() if row.get('orientacion') else ''
        modulo = str(row.get('modulo', '')).strip() if row.get('modulo') else ''
        turno = str(row.get('turno', '')).strip() if row.get('turno') else ''
        horario = str(row.get('horario', '')).strip() if row.get('horario') else ''
        
        # Si todos los campos principales están vacíos, saltar la fila
        if not any([numero, sede, orientacion, modulo, turno, horario]):
            return True
        
        # Si falta algún campo requerido, saltar la fila
        if not numero or not sede or not orientacion or not modulo or not turno or not horario:
            return True
        
        # Validar que el turno sea válido
        if turno not in ['M', 'T', 'V', 'N']:
            return True
        
        return False
    
    class Meta:
        model = Comision
        fields = ('id', 'numero', 'sede', 'orientacion', 'modulo', 
                  'turno', 'horario', 'tutor', 'notas',)
        import_id_fields = ('numero',)
        skip_unchanged = True
        report_skipped = True
