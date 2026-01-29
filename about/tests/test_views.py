"""Tests for About app views."""

from django.test import TestCase
from django.urls import reverse
from about.models import AboutPage, GalleryImage, CollaborationPage


class AboutViewTests(TestCase):
    """Tests for the about() view."""

    def test_about_view_loads(self):
        """GET request should render template and context variable."""
        AboutPage.objects.create(title="Test", content="Hello")

        response = self.client.get(reverse("about"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about/about.html")
        self.assertIn("about_page", response.context)


class GalleryViewTests(TestCase):
    """Tests for the about_gallery() view."""

    def test_gallery_view_loads(self):
        """View should return a context containing images."""
        GalleryImage.objects.create(title="Img1", image="dummy.jpg", description="")

        response = self.client.get(reverse("about_gallery"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about/gallery.html")
        self.assertIn("images", response.context)
        self.assertEqual(len(response.context["images"]), 1)


class CollaborationViewTests(TestCase):
    """Tests for the about_collaborations() view."""

    def test_collaborations_view_loads(self):
        """GET should return template and page content."""
        CollaborationPage.objects.create(content="Info")

        response = self.client.get(reverse("about_collaborations"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about/collaborations_with_farmers.html")
        self.assertIn("collaboration_page", response.context)
