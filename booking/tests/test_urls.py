"""Tests for Booking app URL configuration."""

from django.test import SimpleTestCase
from django.urls import reverse, resolve

from booking.views import (
    book_table,
    my_bookings,
    edit_booking,
    cancel_booking,
    delete_booking,
)


class BookingURLTests(SimpleTestCase):
    """Ensures booking URLs resolve to correct views."""

    def test_book_table_url(self):
        """Reverse lookup for book_table should resolve correctly."""
        url = reverse("book_table")
        self.assertEqual(resolve(url).func, book_table)
        
        
    def test_my_bookings_url(self):
        """Reverse lookup for my_bookings should resolve correctly."""
        url = reverse("my_bookings")
        self.assertEqual(resolve(url).func, my_bookings)
        
        
    def test_edit_booking_url(self):
        """Reverse lookup for edit_booking should resolve correctly."""
        url = reverse("edit_booking", args=[1])
        self.assertEqual(resolve(url).func, edit_booking)
        
        
    def test_cancel_booking_url(self):
        """Reverse lookup for cancel_booking should resolve correctly."""
        url = reverse("cancel_booking", args=[1])
        self.assertEqual(resolve(url).func, cancel_booking)
        
        
    def test_delete_booking_url(self):
        """Reverse lookup for delete_booking should resolve correctly."""
        url = reverse("delete_booking", args=[1])
        self.assertEqual(resolve(url).func, delete_booking)
