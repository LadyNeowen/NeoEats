"""Tests for BookingForm and NewsletterSignupForm."""

from django.test import TestCase
from booking.forms import BookingForm, NewsletterSignupForm


class BookingFormTest(TestCase):
    """Tests for validating BookingForm behavior."""

    def get_valid_data(self):
        """Returns a base valid form submission dictionary."""
        return {
            "name": "John",
            "email": "john@example.com",
            "phone": "123456789",
            "date": "2025-11-25",  # Tuesday
            "time": "17:00",
            "guests": 2,
            "notes": "Test notes",
        }

    def test_form_valid(self):
        """A valid form should pass validation."""
        form = BookingForm(data=self.get_valid_data())
        self.assertTrue(form.is_valid())

    def test_closed_on_monday(self):
        """Form should reject bookings on Mondays."""
        data = self.get_valid_data()
        data["date"] = "2025-11-24"  # Monday
        form = BookingForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("We are closed on Mondays", str(form.errors))

    def test_outside_operating_hours(self):
        """Form should reject times outside valid ranges."""
        data = self.get_valid_data()
        data["time"] = "10:00"
        form = BookingForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("Booking time must be between", str(form.errors))


class NewsletterSignupFormTest(TestCase):
    """Tests for the newsletter signup form."""

    def test_valid_newsletter_form(self):
        """Form should accept a valid email."""
        form = NewsletterSignupForm(data={"email": "test@example.com"})
        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        """Form should reject an invalid email format."""
        form = NewsletterSignupForm(data={"email": "not-an-email"})
        self.assertFalse(form.is_valid())
