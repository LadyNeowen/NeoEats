"""Tests for the Menu app configuration."""

from django.test import SimpleTestCase
from django.apps import apps


class MenuConfigTests(SimpleTestCase):
    """Ensures MenuConfig is correctly set."""

    def test_app_config_name(self):
        """App config name should match the app label."""
        config = apps.get_app_config("menu")
        self.assertEqual(config.name, "menu")
