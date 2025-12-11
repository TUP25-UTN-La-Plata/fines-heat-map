from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Orientacion, Modulo, Comision, Sede

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
        self.assertEqual(str(orientacion), "Matemática")


class ModuloModelTest(TestCase):
    def test_descripcion_obligatoria(self):
        modulo = Modulo(nombre="Historia", descripcion="")
        with self.assertRaises(ValidationError):
            modulo.full_clean()

    def test_str_devuelve_nombre(self):
        modulo = Modulo.objects.create(nombre="Física", descripcion="Test")
        self.assertEqual(str(modulo), "Física")


class ComisionModelTest(TestCase):
    def setUp(self):
        self.sede = Sede.objects.create(nombre="Sede Central")
        self.orientacion = Orientacion.objects.create(nombre="Informática", descripcion="Test")
        self.modulo = Modulo.objects.create(nombre="Matemática", descripcion="Test")

    def test_numero_positivo(self):
        comision = Comision(
            numero=-1,
            sede=self.sede,
            orientacion=self.orientacion,
            modulo=self.modulo,
            turno="Mañana"
        )
        with self.assertRaises(ValidationError):
            comision.full_clean()

    def test_turno_noche_requiere_horario(self):
        comision = Comision(
            numero=1,
            sede=self.sede,
            orientacion=self.orientacion,
            modulo=self.modulo,
            turno="Noche",
            horario=""
        )
        with self.assertRaises(ValidationError):
            comision.full_clean()

    def test_unique_numero_por_sede(self):
        Comision.objects.create(
            numero=1,
            sede=self.sede,
            orientacion=self.orientacion,
            modulo=self.modulo,
            turno="Mañana",
            horario="08:00"
        )
        comision2 = Comision(
            numero=1,
            sede=self.sede,
            orientacion=self.orientacion,
            modulo=self.modulo,
            turno="Tarde",
            horario="14:00"
        )
        with self.assertRaises(ValidationError):
            comision2.full_clean()

    def test_str_devuelve_numero_y_sede(self):
        comision = Comision.objects.create(
            numero=2,
            sede=self.sede,
            orientacion=self.orientacion,
            modulo=self.modulo,
            turno="Mañana",
            horario="09:00"
        )
        self.assertIn("Comisión 2", str(comision))
        self.assertIn("Sede Central", str(comision))