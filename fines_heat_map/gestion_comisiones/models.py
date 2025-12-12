from django.db import models
from django.core.exceptions import ValidationError
from gestion_instituciones.models import Sede
import re


class Orientacion(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - ({self.descripcion})"

    class Meta:
        verbose_name = "Orientación"
        verbose_name_plural = "Orientaciones"
        ordering = ["nombre"]


class Modulo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - ({self.descripcion})"

    class Meta:
        verbose_name = "Módulo"
        verbose_name_plural = "Módulos"
        ordering = ["nombre"]


class Comision(models.Model):

    class Turno(models.TextChoices):
        MANANA = 'M', 'Mañana'
        TARDE = 'T', 'Tarde'
        VESPERTINO = 'V', 'Vespertino'
        NOCHE = 'N', 'Noche'

    sede = models.ForeignKey(Sede, on_delete=models.RESTRICT, related_name='comisiones')
    orientacion = models.ForeignKey(Orientacion, on_delete=models.RESTRICT, related_name='comisiones')
    modulo = models.ForeignKey(Modulo, on_delete=models.RESTRICT, related_name='comisiones')
    numero = models.CharField(
        max_length=50,
        unique=True,
        help_text="Código único de la comisión (Ej: 2024-LP-01)"
    )

    horario = models.CharField(max_length=100, help_text="Días y horarios")
    turno = models.CharField(max_length=1, choices=Turno.choices)
    tutor = models.CharField(max_length=200, blank=True, null=True)
    notas = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return (
            f"{self.numero} - "
            f"({self.sede.nombre}) - "
            f"({self.orientacion.nombre}) - "
            f"({self.modulo.nombre})"
        )

    # VALIDACIONES
    def clean(self):
        # Validación del formato del número de comision (AAAA-XX-00).
        pattern = r"^\d{4}-[A-Za-z]{2}-\d{2}$"
        if not re.match(pattern, self.numero):
            raise ValidationError({
                "numero": "El número debe tener el siguiente formato: 2024-LP-01."
            })

        # Validación para no tener un horario vacio.
        if not self.horario or self.horario.strip() == "":
            raise ValidationError({
                "horario": "El horario no puede estar vacío."
            })

    class Meta:
        verbose_name = "Comisión"
        verbose_name_plural = "Comisiones"
        ordering = ["numero"]
