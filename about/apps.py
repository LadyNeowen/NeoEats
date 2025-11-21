"""
App configuration for the About application.

This app handles:
- About page content
- Collaboration page content
- Gallery images (if included within this app)
"""
from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    Configuration class for the About app.

    Attributes:
        default_auto_field: Specifies the default primary key field type.
        name: The full Python path to the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
