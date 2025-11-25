'''
Admin configuration for NeoEats CMS models.

This module registers the following models with the Django admin:
- AboutPage: Stores content for the About page.
- GalleryImage: Stores images and metadata for the gallery.
- CollaborationPage: Stores content for the collaboration/farmers page.
'''

from django.contrib import admin
from .models import AboutPage, GalleryImage, CollaborationPage

# Register models so they appear in the Django admin interface
admin.site.register(AboutPage)
admin.site.register(GalleryImage)
admin.site.register(CollaborationPage)
