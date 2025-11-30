from django.db import models

class Partido(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

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

    def __str__(self):
        return f"{self.nombre} - ({self.sede_tipo.nombre}) - ({self.localidad.nombre}) - ({self.direccion})"

    class Meta:
        verbose_name = "Sede"
        verbose_name_plural = "Sedes"
        ordering = ["nombre"]