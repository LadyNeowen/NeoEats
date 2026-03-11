"""
URL patterns for the Booking app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_table, name="book_table"),
    path("my-bookings/", views.my_bookings, name="my_bookings"),
    path("edit/<int:booking_id>/", views.edit_booking, name="edit_booking"),
    path("cancel/<int:booking_id>/", views.cancel_booking, name="cancel_booking"),
    path("delete/<int:booking_id>/", views.delete_booking, name="delete_booking"),
]
