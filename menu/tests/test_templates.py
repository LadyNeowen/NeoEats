"""Tests verifying Menu app templates render expected content."""

from django.test import TestCase
from django.urls import reverse
from menu.models import MenuItem


class MenuTemplateTests(TestCase):
    """Tests for menu template content."""

    def test_menu_template_displays_items(self):
        """Menu template should display each category if items exist."""
        MenuItem.objects.create(
            name="Soup",
            category="starter",
            price=8,
        )
        MenuItem.objects.create(
            name="Steak",
            category="main",
            price=20,
        )
        MenuItem.objects.create(
            name="Cake",
            category="dessert",
            price=7,
        )

        response = self.client.get(reverse("menu"))

        self.assertContains(response, "Soup")
        self.assertContains(response, "Steak")
        self.assertContains(response, "Cake")
