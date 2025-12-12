from django.db import models
from gestion_instituciones.models import Sede

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
        INTERMEDIO = 'I', 'Intermedio'

    sede = models.ForeignKey(Sede, on_delete=models.RESTRICT, related_name='comisiones')
    orientacion = models.ForeignKey(Orientacion, on_delete=models.RESTRICT, related_name='comisiones')
    modulo = models.ForeignKey(Modulo, on_delete=models.RESTRICT, related_name='comisiones')
    numero = models.CharField(max_length=50, help_text="Código único de la comisión (Ej: 2024-LP-01)")
    horario = models.CharField(max_length=100, help_text="Días y horarios", blank=True, null=True)
    turno = models.CharField(max_length=1, choices=Turno.choices)
    tutor = models.CharField(max_length=200, blank=True, null=True)
    notas = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.numero} - ({self.sede.nombre}) - ({self.orientacion.nombre}) - ({self.modulo.nombre})"

    class Meta:
        verbose_name = "Comisión"
        verbose_name_plural = "Comisiones"
        ordering = ["numero"]

