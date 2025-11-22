'''
URL patterns for the Booking app.
'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_table, name='book_table'),
]
