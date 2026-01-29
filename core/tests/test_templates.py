"""Tests verifying Core app templates render expected content."""

from django.test import TestCase
from django.urls import reverse


class CoreTemplateTests(TestCase):
    """Ensures templates contain required content."""

    def test_home_template_content(self):
        """Home page should display hero banner text."""
        response = self.client.get(reverse("home"))

        self.assertContains(response, "Welcome to NeoEats")
        self.assertContains(response, "Fresh • Local • Modern Dining")
