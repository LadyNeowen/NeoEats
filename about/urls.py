'''
URL configuration for the About app.

Defines URL patterns for:
- About page
- Gallery page
- Collaborations with Farmers page
'''

from django.urls import path
from . import views

urlpatterns = [
    # Main About page
    path('', views.about, name='about'),

    # Image gallery page
    path('gallery/', views.about_gallery, name='about_gallery'),

    # Collaborations with farmers page
    path(
        'collaborations-with-farmers/',
        views.about_collaborations,
        name='about_collaborations'
    ),
]
