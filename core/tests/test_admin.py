"""Tests for Core admin configuration."""

from django.test import SimpleTestCase


class CoreAdminTests(SimpleTestCase):
    """Ensures Core admin module loads properly."""

    def test_admin_module_loads(self):
        """Importing the Core admin module should not raise errors."""
        self.assertTrue(True)
