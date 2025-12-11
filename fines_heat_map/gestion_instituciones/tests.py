from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Partido, Localidad, SedeTipo, Sede

class PartidoModelTest(TestCase):
    def test_nombre_minimo_caracteres(self):
        partido = Partido(nombre="AB")
        with self.assertRaises(ValidationError):
            partido.full_clean()

    def test_nombre_unico(self):
        Partido.objects.create(nombre="La Plata")
        partido2 = Partido(nombre="La Plata")
        with self.assertRaises(ValidationError):
            partido2.full_clean()

    def test_str_devuelve_nombre(self):
        partido = Partido.objects.create(nombre="Berisso")
        self.assertEqual(str(partido), "Berisso")


class LocalidadModelTest(TestCase):
    def setUp(self):
        self.partido = Partido.objects.create(nombre="La Plata")

    def test_codigo_postal_valido(self):
        localidad = Localidad(nombre="Villa Elvira", codigo_postal=999, partido=self.partido)
        with self.assertRaises(ValidationError):
            localidad.full_clean()

    def test_unique_nombre_por_partido(self):
        Localidad.objects.create(nombre="Villa Elvira", codigo_postal=1900, partido=self.partido)
        localidad2 = Localidad(nombre="Villa Elvira", codigo_postal=1901, partido=self.partido)
        with self.assertRaises(ValidationError):
            localidad2.full_clean()

    def test_str_devuelve_nombre_y_partido(self):
        localidad = Localidad.objects.create(nombre="Tolosa", codigo_postal=1900, partido=self.partido)
        self.assertIn("Tolosa", str(localidad))
        self.assertIn("La Plata", str(localidad))


class SedeTipoModelTest(TestCase):
    def test_descripcion_obligatoria(self):
        sede_tipo = SedeTipo(nombre="Universidad", descripcion="")
        with self.assertRaises(ValidationError):
            sede_tipo.full_clean()

    def test_nombre_unico(self):
        SedeTipo.objects.create(nombre="Escuela", descripcion="Institución educativa")
        sede_tipo2 = SedeTipo(nombre="Escuela", descripcion="Otra descripción")
        with self.assertRaises(ValidationError):
            sede_tipo2.full_clean()

    def test_str_devuelve_nombre(self):
        sede_tipo = SedeTipo.objects.create(nombre="Instituto", descripcion="Centro de estudios")
        self.assertEqual(str(sede_tipo), "Instituto")


class SedeModelTest(TestCase):
    def setUp(self):
        self.partido = Partido.objects.create(nombre="La Plata")
        self.localidad = Localidad.objects.create(nombre="Villa Elvira", codigo_postal=1900, partido=self.partido)
        self.sede_tipo = SedeTipo.objects.create(nombre="Escuela", descripcion="Institución educativa")

    def test_coordenadas_obligatorias(self):
        sede = Sede(
            nombre="Sede Central",
            sede_tipo=self.sede_tipo,
            localidad=self.localidad,
            direccion="Calle 123",
            telefono="+54123456789",
            email="test@example.com",
            lat=None,
            long=None
        )
        with self.assertRaises(ValidationError):
            sede.full_clean()

    def test_unique_nombre_por_localidad(self):
        Sede.objects.create(
            nombre="Sede Central",
            sede_tipo=self.sede_tipo,
            localidad=self.localidad,
            direccion="Calle 123",
            telefono="+54123456789",
            email="test@example.com",
            lat=-34.921,
            long=-57.954
        )
        sede2 = Sede(
            nombre="Sede Central",
            sede_tipo=self.sede_tipo,
            localidad=self.localidad,
            direccion="Calle 456",
            telefono="+54123456780",
            email="otro@example.com",
            lat=-34.922,
            long=-57.955
        )
        with self.assertRaises(ValidationError):
            sede2.full_clean()

    def test_str_devuelve_nombre_y_localidad(self):
        sede = Sede.objects.create(
            nombre="Sede Norte",
            sede_tipo=self.sede_tipo,
            localidad=self.localidad,
            direccion="Calle 789",
            telefono="+54123456781",
            email="norte@example.com",
            lat=-34.920,
            long=-57.950
        )
        self.assertIn("Sede Norte", str(sede))
        self.assertIn("Villa Elvira", str(sede))