from rest_framework import serializers
from .models import Sede
from gestion_comisiones.models import Comision

class ComisionInfoSerializer(serializers.ModelSerializer):
    orientacion_nombre = serializers.CharField(source='orientacion.nombre', read_only=True)
    modulo_nombre = serializers.CharField(source='modulo.nombre', read_only=True)
    turno_nombre = serializers.CharField(source='get_turno_display', read_only=True)

    class Meta:
        model = Comision
        fields = [
            'id', 
            'numero', 
            'orientacion_nombre', 
            'modulo_nombre', 
            'turno_nombre', 
            'horario', 
            'tutor'
        ]


class SedeCompletaSerializer(serializers.ModelSerializer):
    tipo_nombre = serializers.CharField(source='sede_tipo.nombre', read_only=True, default="")
    localidad_nombre = serializers.CharField(source='localidad.nombre', read_only=True, default="")
    partido_nombre = serializers.CharField(source='localidad.partido.nombre', read_only=True, default="")
    cp = serializers.CharField(source='localidad.codigo_postal', read_only=True, default="")

    lat = serializers.FloatField(read_only=True)
    long = serializers.FloatField(read_only=True)

    comisiones = ComisionInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Sede
        fields = [
            'id',
            'nombre',
            'tipo_nombre',
            'direccion',
            'localidad_nombre',
            'partido_nombre',
            'cp',
            'lat',
            'long',
            'telefono',
            'email',
            'notas',
            'comisiones',
        ]