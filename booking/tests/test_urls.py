"""Tests for Booking app URL configuration."""

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from booking.views import book_table


class BookingURLTests(SimpleTestCase):
    """Ensures booking URLs resolve to correct views."""

    def test_book_table_url(self):
        """Reverse lookup for book_table should resolve correctly."""
        url = reverse("book_table")
        self.assertEqual(resolve(url).func, book_table)
