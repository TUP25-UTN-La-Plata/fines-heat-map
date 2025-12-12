class UrlsTestCase(TestCase):
    def test_home_url_resolves(self):
        resolver = resolve(reverse("home"))
        self.assertEqual(resolver.func.__name__, home.__name__)