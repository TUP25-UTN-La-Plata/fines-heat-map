from django.test import TestCase
from django.urls import reverse


class SmokeRoutesTestCase(TestCase):
    """Valida que las rutas principales respondan sin errores de enrutado."""

    def test_home_responde_ok(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_mapa_responde_ok(self):
        response = self.client.get(reverse("heatmap:mapa"))
        self.assertEqual(response.status_code, 200)

    def test_instituciones_responde_ok(self):
        response = self.client.get(reverse("instituciones:lista_instituciones"))
        self.assertEqual(response.status_code, 200)

    def test_comisiones_responde_ok(self):
        response = self.client.get(reverse("comisiones:comisiones"))
        self.assertEqual(response.status_code, 200)

    def test_admin_redirige_a_login(self):
        response = self.client.get("/admin/")
        self.assertIn(response.status_code, [302, 301])


class HeatmapApiTestCase(TestCase):
    """Cubre el endpoint JSON base del mapa."""

    def test_api_sedes_responde_json(self):
        response = self.client.get(reverse("heatmap:get_sedes_data"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertIsInstance(response.json(), list)
