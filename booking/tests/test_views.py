"""Tests for booking app views."""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from booking.models import Booking, NewsletterSignup


class BookingViewTest(TestCase):
    """Tests for the book_table view."""

    def setUp(self):
        """
        Create and log in a test user before each test.
        This is needed because the booking view requires authentication.
        """
        User = get_user_model()

        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )

        self.client.login(username="testuser", password="testpass123")

    def test_get_request_renders_template(self):
        """GET request should render the booking template."""
        response = self.client.get(reverse("book_table"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "booking/book_table.html")
        self.assertIn("form", response.context)
        self.assertIn("newsletter_form", response.context)

    def test_valid_booking_submission(self):
        """POST booking form should create a booking and redirect."""
        response = self.client.post(
            reverse("book_table"),
            {
                "submit_booking": "",
                "name": "John",
                "email": "john@example.com",
                "phone": "12345",
                "date": "2026-01-29",  # Thursday
                "time": "17:00",
                "guests": 2,
            },
        )

        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("my_bookings"))

    def test_valid_newsletter_submission(self):
        """POST newsletter form should add a subscriber and redirect."""
        response = self.client.post(
            reverse("book_table"),
            {
                "submit_newsletter": "",
                "email": "test@example.com",
            },
        )

        self.assertEqual(NewsletterSignup.objects.count(), 1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("book_table"))

    def test_invalid_monday_booking(self):
        """Bookings on Monday should be rejected with an error."""
        response = self.client.post(
            reverse("book_table"),
            {
                "submit_booking": "",
                "name": "John",
                "email": "john@example.com",
                "phone": "12345",
                "date": "2026-02-02",  # Monday
                "time": "17:00",
                "guests": 2,
            },
        )

        self.assertEqual(Booking.objects.count(), 0)
        self.assertContains(response, "We are closed on Mondays")
