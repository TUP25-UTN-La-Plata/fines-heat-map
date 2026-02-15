from django.test import TestCase
from django.urls import reverse


class ComisionesViewsAndApiTestCase(TestCase):
    """Pruebas mínimas del módulo de comisiones y sus APIs de catálogos."""

    def test_comisiones_view_ok(self):
        response = self.client.get(reverse("comisiones:comisiones"))
        self.assertEqual(response.status_code, 200)

    def test_api_modulos_ok(self):
        response = self.client.get(reverse("comisiones:api_modulos"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertIsInstance(response.json(), list)

    def test_api_orientaciones_ok(self):
        response = self.client.get(reverse("comisiones:api_orientaciones"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertIsInstance(response.json(), list)
