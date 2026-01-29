"""
Views for the About app.

Handles rendering of:
- The About page
- The Gallery page
- The Collaborations With Farmers page
"""

from django.shortcuts import render
from .models import AboutPage, GalleryImage, CollaborationPage


def about(request):
    """
    Render the About page.

    Retrieves:
        The first AboutPage instance (expected to be a single-entry model).

    Template:
        about/about.html

    Context:
        about_page (AboutPage): Content for the About page.
    """
    about_page = AboutPage.objects.first()
    return render(request, "about/about.html", {"about_page": about_page})


def about_gallery(request):
    """
    Render the Gallery page.

    Retrieves:
        All GalleryImage instances.

    Template:
        about/gallery.html

    Context:
        images (QuerySet[GalleryImage]): List of images to display.
    """
    images = GalleryImage.objects.all()
    return render(
        request,
        "about/gallery.html",
        {"images": images},
    )


def about_collaborations(request):
    """
    Render the Collaborations With Farmers page.

    Retrieves:
        The first CollaborationPage instance
        (expected to be a single-entry model).

    Template:
        about/collaborations_with_farmers.html

    Context:
        collaboration_page (CollaborationPage): Page content.
    """
    collaboration_page = CollaborationPage.objects.first()
    return render(
        request,
        "about/collaborations_with_farmers.html",
        {"collaboration_page": collaboration_page},
    )
