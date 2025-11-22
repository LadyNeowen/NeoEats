'''
URL patterns for the Menu app.
'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
]
