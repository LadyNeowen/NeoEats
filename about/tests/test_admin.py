"""Tests for Django admin configuration of About app."""

from django.test import TestCase
from django.contrib import admin
from about.models import AboutPage, GalleryImage, CollaborationPage


class AdminRegistrationTests(TestCase):
    """Tests that models are correctly registered in the admin site."""

    def test_about_page_registered(self):
        """AboutPage should be registered with the admin."""
        self.assertIn(AboutPage, admin.site._registry)

    def test_gallery_image_registered(self):
        """GalleryImage should be registered with the admin."""
        self.assertIn(GalleryImage, admin.site._registry)

    def test_collaboration_page_registered(self):
        """CollaborationPage should be registered with the admin."""
        self.assertIn(CollaborationPage, admin.site._registry)
