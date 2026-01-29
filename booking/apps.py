"""
App configuration for the Booking app.
"""

from django.apps import AppConfig


class BookingConfig(AppConfig):
    """Configuration for the Booking app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "booking"
