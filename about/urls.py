from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    
    path('how-it-all-started/', views.how_it_all_started, name='about_story'),
    path('gallery/', views.gallery, name='about_gallery'),
    path('collaborations-with-farmers/', views.collaborations_with_farmers, name='about_collaborations'),
]