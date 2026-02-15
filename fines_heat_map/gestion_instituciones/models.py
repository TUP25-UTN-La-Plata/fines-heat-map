from django.db import models
from django.core.exceptions import ValidationError
import re


class Partido(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def clean(self):
        if not self.nombre or self.nombre.strip() == "":
            raise ValidationError({"nombre": "El nombre del partido no puede estar vacío."})

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name = "Partido"
        verbose_name_plural = "Partidos"
        ordering = ["nombre"]


class Localidad(models.Model):
    partido = models.ForeignKey(Partido, on_delete=models.RESTRICT, related_name="localidades")
    nombre = models.CharField(max_length=100, unique=True)
    codigo_postal = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def clean(self):
        # Validación que impide ingresar un nombre vacio.
        if not self.nombre or self.nombre.strip() == "":
            raise ValidationError({"nombre": "El nombre de la localidad no puede estar vacío."})

        # Validación que solo permite ingresar un codigo postal alfanumerico.
        if self.codigo_postal and not re.match(r"^[A-Za-z0-9]+$", self.codigo_postal):
            raise ValidationError({"codigo_postal": "El código postal solo puede contener letras y números, sin espacios."})

    def __str__(self):
        return f"{self.nombre} - ({self.partido.nombre})"

    class Meta:
        verbose_name = "Localidad"
        verbose_name_plural = "Localidades"
        ordering = ["nombre"]


class SedeTipo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    # Valiadción que impide ingresar un tipo de sede vacio.
    def clean(self):
        if not self.nombre or self.nombre.strip() == "":
            raise ValidationError({"nombre": "El nombre del tipo de sede no puede estar vacío."})

    def __str__(self):
        return f"{self.nombre} - ({self.descripcion})"

    class Meta:
        verbose_name = "Tipo de Sede"
        verbose_name_plural = "Tipos de Sede"
        ordering = ["nombre"]


class Sede(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    sede_tipo = models.ForeignKey(SedeTipo, on_delete=models.RESTRICT, related_name="sedes")
    direccion = models.CharField(max_length=200)
    localidad = models.ForeignKey(Localidad, on_delete=models.RESTRICT, related_name="sedes")
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    long = models.DecimalField(max_digits=10, decimal_places=6)
    notas = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def clean(self):
        # Validación que impide ingresar un nombre de sede vacio.
        if not self.nombre or self.nombre.strip() == "":
            raise ValidationError({"nombre": "El nombre de la sede no puede estar vacío."})

        # Validación para el formato de numeros telefonicos.
        if self.telefono:
            if not re.match(r"^[0-9\s\-]+$", self.telefono):
                raise ValidationError({
                    "telefono": "El teléfono solo puede contener números, espacios o guiones."
                })

        # Validación de Latitud.
        if self.lat < -90 or self.lat > 90:
            raise ValidationError({"lat": "La latitud debe estar entre -90 y 90."})

        # Validación de Longitud.
        if self.long < -180 or self.long > 180:
            raise ValidationError({"long": "La longitud debe estar entre -180 y 180."})

    def __str__(self):
        return f"{self.nombre} - ({self.sede_tipo.nombre}) - ({self.localidad.nombre}) - ({self.direccion})"

    class Meta:
        verbose_name = "Sede"
        verbose_name_plural = "Sedes"
        ordering = ["nombre"]
