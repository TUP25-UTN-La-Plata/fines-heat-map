from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from gestion_instituciones.models import Sede

class Orientacion(models.Model):
    nombre = models.CharField(
        max_length=100,
        unique=True,
        validators=[RegexValidator(r'^[A-Za-z\s]+$', 'Solo letras y espacios')]
    )
    descripcion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def clean(self):
        if len(self.nombre) < 3:
            raise ValidationError("El nombre de la orientación debe tener al menos 3 caracteres.")

    class Meta:
        verbose_name = "Orientación"
        verbose_name_plural = "Orientaciones"
        ordering = ["nombre"]
        constraints = [
            models.UniqueConstraint(fields=['nombre'], name='unique_orientacion_nombre')
        ]

    def __str__(self):
        return f"{self.nombre} - ({self.descripcion})"


class Modulo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def clean(self):
        if not self.descripcion:
            raise ValidationError("El módulo debe tener una descripción.")

    class Meta:
        verbose_name = "Módulo"
        verbose_name_plural = "Módulos"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} - ({self.descripcion})"


class Comision(models.Model):
    class Turno(models.TextChoices):
        MANANA = 'M', 'Mañana'
        TARDE = 'T', 'Tarde'
        VESPERTINO = 'V', 'Vespertino'
        NOCHE = 'N', 'Noche'

    sede = models.ForeignKey(Sede, on_delete=models.RESTRICT, related_name='comisiones')
    orientacion = models.ForeignKey(Orientacion, on_delete=models.RESTRICT, related_name='comisiones')
    modulo = models.ForeignKey(Modulo, on_delete=models.RESTRICT, related_name='comisiones')
    numero = models.CharField(max_length=50, help_text="Código único de la comisión (Ej: 2024-LP-01)")
    horario = models.CharField(max_length=100, help_text="Días y horarios", blank=True, null=True)
    turno = models.CharField(max_length=1, choices=Turno.choices)
    tutor = models.CharField(max_length=200, blank=True, null=True,
                             validators=[RegexValidator(r'^[A-Za-z\s]+$', 'Solo letras y espacios')])
    notas = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def clean(self):
        if self.turno == Comision.Turno.NOCHE and not self.horario:
            raise ValidationError("Las comisiones nocturnas deben tener horario definido.")

    class Meta:
        verbose_name = "Comisión"
        verbose_name_plural = "Comisiones"
        ordering = ["numero"]
        constraints = [
            models.UniqueConstraint(fields=['numero', 'sede'], name='unique_comision_por_sede')
        ]

    def __str__(self):
        return f"{self.numero} - ({self.sede.nombre}) - ({self.orientacion.nombre}) - ({self.modulo.nombre})"
