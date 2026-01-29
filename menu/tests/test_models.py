"""Tests for Menu app models."""

from django.test import TestCase
from menu.models import MenuItem


class MenuItemModelTests(TestCase):
    """Tests for the MenuItem model."""

    def test_str_method(self):
        """__str__ should include name and display category."""
        item = MenuItem.objects.create(
            name="Soup",
            category="starter",
            price=10,
        )
        self.assertEqual(str(item), "Soup (Starter)")

    def test_category_choices(self):
        """MenuItem should enforce category choices."""
        item = MenuItem.objects.create(
            name="Cake",
            category="dessert",
            price=12,
        )
        self.assertEqual(item.get_category_display(), "Dessert")
