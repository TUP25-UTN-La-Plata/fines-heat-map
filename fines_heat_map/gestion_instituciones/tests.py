from django.test import TestCase
from django.urls import reverse


class InstitucionesRoutesTestCase(TestCase):
    """Pruebas mínimas de vistas públicas de instituciones."""

    def test_lista_instituciones_ok(self):
        response = self.client.get(reverse("instituciones:lista_instituciones"))
        self.assertEqual(response.status_code, 200)
