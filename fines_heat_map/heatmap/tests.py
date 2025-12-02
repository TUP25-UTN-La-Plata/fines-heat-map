from django.test import TestCase
from django.urls import reverse, resolve
from django.http import HttpResponse
from .views import home


class UrlsTestCase(TestCase):
    def test_home_url_resolves(self):
        """Verifica que la URL raíz ('/') apunte a la vista home"""
        resolver = resolve(reverse("home"))
        self.assertEqual(resolver.func, home)

    def test_home_url_response(self):
        """Verifica que la URL raíz devuelva un código 200 (OK)"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_mapa_url_includes_namespace(self):
        """Verifica que la URL 'mapa/' esté registrada con el namespace correcto"""
        resolver = resolve("/mapa/")
        self.assertEqual(resolver.namespace, "heatmap")

    def test_instituciones_url_includes_namespace(self):
        """Verifica que la URL 'instituciones/' esté registrada con el namespace correcto"""
        resolver = resolve("/instituciones/")
        self.assertEqual(resolver.namespace, "instituciones")

    def test_comisiones_url_includes_namespace(self):
        """Verifica que la URL 'comisiones/' esté registrada con el namespace correcto"""
        resolver = resolve("/comisiones/")
        self.assertEqual(resolver.namespace, "comisiones")

#test de integracion simple para verificar que las vistas principales respondan correctamente

class IntegrationUrlsTestCase(TestCase):
    def test_home_view(self):
        """La vista principal debe responder con 200 y contener texto esperado"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bienvenido")  # Ajusta según tu template

    def test_heatmap_index(self):
        """La vista inicial de heatmap debe responder correctamente"""
        response = self.client.get(reverse("heatmap:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mapa de calor")  # Ajusta al contenido real

    def test_instituciones_index(self):
        """La vista inicial de instituciones debe responder correctamente"""
        response = self.client.get(reverse("instituciones:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Instituciones")  # Ajusta al contenido real

    def test_comisiones_index(self):
        """La vista inicial de comisiones debe responder correctamente"""
        response = self.client.get(reverse("comisiones:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Comisiones")  # Ajusta al contenido real
