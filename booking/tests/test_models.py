'''Tests for the Booking app models.'''

from django.test import TestCase
from booking.models import Booking, NewsletterSignup
from datetime import date, time


class BookingModelTest(TestCase):
    '''Tests for the Booking model.'''

    def test_booking_str(self):
        '''The __str__ method should return formatted booking details.'''
        booking = Booking.objects.create(
            name='John Doe',
            phone='12345678',
            email='john@example.com',
            date=date(2025, 11, 27),
            time=time(18, 0),
            guests=2,
        )
        expected = 'Booking for John Doe on 2025-11-27 at 18:00:00'
        self.assertEqual(str(booking), expected)

    def test_unique_date_time_constraint(self):
        '''Booking should enforce unique date + time combinations.'''
        Booking.objects.create(
            name='A',
            phone='1',
            email='a@example.com',
            date=date(2025, 11, 27),
            time=time(18, 0),
            guests=2,
        )
        with self.assertRaises(Exception):
            Booking.objects.create(
                name='B',
                phone='2',
                email='b@example.com',
                date=date(2025, 11, 27),
                time=time(18, 0),
                guests=4,
            )


class NewsletterSignupTest(TestCase):
    '''Tests for the NewsletterSignup model.'''

    def test_str_method(self):
        '''The __str__ method should display the email.'''
        signup = NewsletterSignup.objects.create(email='hello@example.com')
        self.assertEqual(str(signup), 'hello@example.com')

    def test_unique_email_constraint(self):
        '''Newsletter signup email must be unique.'''
        NewsletterSignup.objects.create(email='test@example.com')
        with self.assertRaises(Exception):
            NewsletterSignup.objects.create(email='test@example.com')
