from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError

class Partido(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def clean(self):
        if len(self.nombre) < 3:
            raise ValidationError("El nombre del partido debe tener al menos 3 caracteres.")

    class Meta:
        verbose_name = "Partido"
        verbose_name_plural = "Partidos"
        ordering = ["nombre"]
        constraints = [
            models.UniqueConstraint(fields=['nombre'], name='unique_partido_nombre')
        ]

    def __str__(self):
        return self.nombre


class Localidad(models.Model):
    partido = models.ForeignKey(Partido, on_delete=models.RESTRICT, related_name="localidades")
    nombre = models.CharField(max_length=100)
    codigo_postal = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def clean(self):
        if self.codigo_postal < 1000 or self.codigo_postal > 9999:
            raise ValidationError("El código postal debe ser un número de 4 dígitos.")

    class Meta:
        verbose_name = "Localidad"
        verbose_name_plural = "Localidades"
        ordering = ["nombre"]
        constraints = [
            models.UniqueConstraint(fields=['nombre', 'partido'], name='unique_localidad_por_partido')
        ]

    def __str__(self):
        return f"{self.nombre} - ({self.partido.nombre})"


class SedeTipo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def clean(self):
        if not self.descripcion:
            raise ValidationError("La descripción del tipo de sede no puede estar vacía.")

    class Meta:
        verbose_name = "Tipo de Sede"
        verbose_name_plural = "Tipos de Sede"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Sede(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    sede_tipo = models.ForeignKey(SedeTipo, on_delete=models.RESTRICT, related_name="sedes")
    direccion = models.CharField(max_length=200)
    localidad = models.ForeignKey(Localidad, on_delete=models.RESTRICT, related_name="sedes")
    telefono = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\+?\d{7,15}$', 'Número de teléfono inválido')],
        blank=True, null=True
    )
    email = models.EmailField(validators=[EmailValidator()], blank=True, null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    long = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    notas = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def clean(self):
        if not self.lat or not self.long:
            raise ValidationError("La sede debe tener coordenadas geográficas definidas (latitud y longitud).")

    class Meta:
        verbose_name = "Sede"
        verbose_name_plural = "Sedes"
        ordering = ["nombre"]
        constraints = [
            models.UniqueConstraint(fields=['nombre', 'localidad'], name='unique_sede_por_localidad')
        ]

    def __str__(self):
        return f"{self.nombre} - ({self.sede_tipo.nombre}) - ({self.localidad.nombre}) - ({self.direccion})"