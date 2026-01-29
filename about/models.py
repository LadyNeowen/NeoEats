"""
Models for the NeoEats content management system.

This module defines database models for:
- AboutPage: Stores content for the About page
- GalleryImage: Stores images and metadata for the Gallery
- CollaborationPage: Stores content for the Collaborations page
"""

from django.db import models
from cloudinary.models import CloudinaryField


class AboutPage(models.Model):
    """
    Represents the About page content.

    Fields:
        title (CharField): The heading/title displayed on the About page.
        content (TextField): The main body text of the About page.
    """

    title = models.CharField(max_length=200, default="About NeoEats")
    content = models.TextField()

    def __str__(self):
        return "About Page Content"


class GalleryImage(models.Model):
    """
    Represents an image entry in the Gallery.

    Fields:
        title (CharField): The display name of the image.
        description (TextField): Optional descriptive text for the image.
        image (CloudinaryField): The uploaded image file.
    """

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300, blank=True)
    image = CloudinaryField("image")

    def __str__(self):
        return self.title


class CollaborationPage(models.Model):
    """
    Represents the content of the Collaborations page.

    Fields:
        title (CharField): The heading/title for the page.
        content (TextField): The main descriptive text about collaborations.
    """

    title = models.CharField(max_length=200, default="Working With Our Farmers")
    content = models.TextField()

    def __str__(self):
        return "Collaborations Page Content"
