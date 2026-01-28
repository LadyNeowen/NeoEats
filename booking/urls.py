'''
URL patterns for the Booking app.
'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_table, name='book_table'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('<int:booking_id>/edit/', views.edit_booking, name='edit_booking'),
    path('<int:booking_id>/cancel/', views.cancel_booking, name='cancel_booking'),
]
