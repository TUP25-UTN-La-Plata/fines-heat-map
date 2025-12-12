from django.test import TestCase
from django.core.exceptions import ValidationError
from gestion_instituciones.models import Sede
from .models import Orientacion, Modulo, Comision

class OrientacionModelTest(TestCase):
    def test_nombre_obligatorio(self):
        orientacion = Orientacion(nombre="", descripcion="Test")
        with self.assertRaises(ValidationError):
            orientacion.full_clean()

    def test_nombre_minimo_caracteres(self):
        orientacion = Orientacion(nombre="AB", descripcion="Test")
        with self.assertRaises(ValidationError):
            orientacion.full_clean()

    def test_nombre_unico(self):
        Orientacion.objects.create(nombre="Informática", descripcion="Test")
        orientacion2 = Orientacion(nombre="Informática", descripcion="Otro")
        with self.assertRaises(ValidationError):
            orientacion2.full_clean()

    def test_str_devuelve_nombre(self):
        orientacion = Orientacion.objects.create(nombre="Matemática", descripcion="Test")
        self.assertIn("Matemática", str(orientacion))


class ModuloModelTest(TestCase):
    def test_descripcion_obligatoria(self):
        modulo = Modulo(nombre="Historia", descripcion="")
        with self.assertRaises(ValidationError):
            modulo.full_clean()

    def test_str_devuelve_nombre(self):
        modulo = Modulo.objects.create(nombre="Física", descripcion="Test")
        self.assertIn("Física", str(modulo))


class ComisionModelTest(TestCase):
    def setUp(self):
        self.sede = Sede.objects.create(nombre="Sede Central")
        self.orientacion = Orientacion.objects.create(nombre="Informática", descripcion="Test")
        self.modulo = Modulo.objects.create(nombre="Matemática", descripcion="Test")

    def test_numero_obligatorio(self):
        comision = Comision(
            numero="",
            sede=self.sede,
            orientacion=self.orientacion,
            modulo=self.modulo,
            turno=Comision.Turno.MANANA
        )
        with self.assertRaises(ValidationError):
            comision.full_clean()

    def test_turno_noche_requiere_horario(self):
        comision = Comision(
            numero="2024-LP-01",
            sede=self.sede,
            orientacion=self.orientacion,
            modulo=self.modulo,
            turno=Comision.Turno.NOCHE,
            horario=""
        )
        with self.assertRaises(ValidationError):
            comision.full_clean()

    def test_unique_numero_por_sede(self):
        Comision.objects.create(
            numero="2024-LP-01",
            sede=self.sede,
            orientacion=self.orientacion,
            modulo=self.modulo,
            turno=Comision.Turno.MANANA,
            horario="08:00"
        )
        comision2 = Comision(
            numero="2024-LP-01",
            sede=self.sede,
            orientacion=self.orientacion,
            modulo=self.modulo,
            turno=Comision.Turno.TARDE,
            horario="14:00"
        )
        with self.assertRaises(ValidationError):
            comision2.full_clean()

    def test_str_devuelve_numero_y_sede(self):
        comision = Comision.objects.create(
            numero="2024-LP-02",
            sede=self.sede,
            orientacion=self.orientacion,
            modulo=self.modulo,
            turno=Comision.Turno.MANANA,
            horario="09:00"
        )
        self.assertIn("2024-LP-02", str(comision))
        self.assertIn("Sede Central", str(comision))