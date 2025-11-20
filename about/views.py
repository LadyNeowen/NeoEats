from django.shortcuts import render
from .models import AboutPage, GalleryImage, CollaborationPage


def about(request):
    about_page = AboutPage.objects.first()
    return render(request, "about/about.html", {"about_page": about_page})


def about_gallery(request):
    images = GalleryImage.objects.all()
    return render(request, "about/gallery.html", {"images": images})


def about_collaborations(request):
    collaboration_page = CollaborationPage.objects.first()
    return render(request, "about/collaborations_with_farmers.html",
                  {"collaboration_page": collaboration_page})
