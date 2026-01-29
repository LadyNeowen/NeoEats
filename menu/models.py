"""
Models for the Menu app.

Includes:
- MenuItem: Represents a menu entry such as a starter, main course, or dessert.
"""

from django.db import models


class MenuItem(models.Model):
    """Represents a single dish in the restaurant menu."""

    CATEGORY_CHOICES = [
        ("starter", "Starter"),
        ("main", "Main Course"),
        ("dessert", "Dessert"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=0)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    vegetarian = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
