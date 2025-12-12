from django.test import TestCase
from django.urls import reverse, resolve
from heatmap.views import home

class UrlsTestCase(TestCase):
    def test_home_url_resolves(self):
        resolver = resolve(reverse("home"))
        self.assertEqual(resolver.func.__name__, home.__name__)  # comparar nombres

    def test_home_url_response(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_mapa_url_includes_namespace(self):
        resolver = resolve("/mapa/")
        self.assertEqual(resolver.namespace, "heatmap")  # requiere app_name en heatmap/urls.py

    def test_instituciones_url_includes_namespace(self):
        resolver = resolve("/instituciones/")
        self.assertEqual(resolver.namespace, "instituciones")  # requiere app_name en gestion_instituciones/urls.py

    def test_comisiones_url_includes_namespace(self):
        resolver = resolve("/comisiones/")
        self.assertEqual(resolver.namespace, "comisiones")  # requiere app_name en gestion_comisiones/urls.py


class IntegrationUrlsTestCase(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bienvenido")  # ajusta al texto real del template

    def test_heatmap_index(self):
        response = self.client.get(reverse("heatmap:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mapa de calor")  # ajusta al texto real del template