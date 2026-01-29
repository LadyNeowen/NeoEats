"""
Admin configuration for the Menu app.
Registers menu items for management in Django admin.
"""

from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """Admin configuration for MenuItem objects."""

    list_display = ("name", "category", "price", "vegetarian", "gluten_free")
    list_filter = ("category", "vegetarian", "gluten_free")
    search_fields = ("name", "description")
