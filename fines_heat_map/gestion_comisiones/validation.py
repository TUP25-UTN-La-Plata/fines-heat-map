from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator, EmailValidator
from django.core.exceptions import ValidationError

class Orientacion(models.Model):
    nombre = models.CharField(
        max_length=100,
        unique=True,
        validators=[RegexValidator(r'^[A-Za-z\s]+$', 'Solo letras y espacios')]
    )
    descripcion = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def clean(self):
        # Validación personalizada
        if len(self.nombre) < 3:
            raise ValidationError("El nombre de la orientación debe tener al menos 3 caracteres.")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nombre'], name='unique_orientacion_nombre')
        ]

    def __str__(self):
        return self.nombre


class Modulo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def clean(self):
        if not self.descripcion:
            raise ValidationError("El módulo debe tener una descripción.")

    def __str__(self):
        return self.nombre


class Comision(models.Model):
    numero = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    sede = models.ForeignKey("Sede", on_delete=models.PROTECT)
    orientacion = models.ForeignKey(Orientacion, on_delete=models.PROTECT)
    modulo = models.ForeignKey(Modulo, on_delete=models.PROTECT)
    turno = models.CharField(max_length=20, choices=[("Mañana", "Mañana"), ("Tarde", "Tarde"), ("Noche", "Noche")])
    horario = models.CharField(max_length=50, blank=True)
    tutor = models.CharField(max_length=100, validators=[RegexValidator(r'^[A-Za-z\s]+$', 'Solo letras y espacios')])
    notas = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def clean(self):
        # Ejemplo de validación cruzada
        if self.turno == "Noche" and not self.horario:
            raise ValidationError("Las comisiones nocturnas deben tener horario definido.")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['numero', 'sede'], name='unique_comision_por_sede')
        ]

    def __str__(self):
        return f"Comisión {self.numero} - {self.sede}"