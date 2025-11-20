from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('gallery/', views.about_gallery, name='about_gallery'),
    path('collaborations-with-farmers/', views.about_collaborations, name='about_collaborations'),
]