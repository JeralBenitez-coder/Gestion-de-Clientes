from django.test import SimpleTestCase
from django.urls import get_resolver


class UrlsImportTest(SimpleTestCase):
    def test_project_urls_import(self):
        resolver = get_resolver()
        self.assertTrue(hasattr(resolver, 'url_patterns'))
