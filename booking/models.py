"""
Models for the Booking app.

Includes:
- Booking: Table reservation details.
- NewsletterSignup: Email subscription entries.
"""

from django.db import models
from django.conf import settings


class Booking(models.Model):
    """Represents a table reservation at NeoEats."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookings",
        null=True,
        blank=True,
    )

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("cancelled", "Cancelled"),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    date = models.DateField()
    time = models.TimeField()

    guests = models.PositiveIntegerField()
    notes = models.TextField(blank=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="pending",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("date", "time")  # Prevent double bookings

    def __str__(self):
        return f"Booking for {self.name} on {self.date} at {self.time}"


class NewsletterSignup(models.Model):
    """Stores newsletter subscriber email addresses."""

    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
