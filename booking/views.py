from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.db import IntegrityError
from django.conf import settings   # <-- IMPORTANT

from .forms import BookingForm, NewsletterSignupForm
from .models import Booking


def book_table(request):
    """
    Display and process the booking form and newsletter signup form.
    """
    if request.method == 'POST':

        # Booking form submitted
        if 'submit_booking' in request.POST:
            booking_form = BookingForm(request.POST)
            newsletter_form = NewsletterSignupForm()

            if booking_form.is_valid():
                try:
                    booking = booking_form.save()

                    # ---------------------------
                    #   EMAIL ONLY IN DEBUG MODE
                    # ---------------------------
                    if settings.DEBUG:
                        send_mail(
                            subject='Your NeoEats Booking Confirmation',
                            message=f'''
Thank you for booking a table at NeoEats!

Here are your booking details:
Name: {booking.name}
Date: {booking.date}
Time: {booking.time}
Guests: {booking.guests}

We look forward to seeing you!
''',
                            from_email='neoeats@example.com',
                            recipient_list=[booking.email],
                            fail_silently=False,
                        )

                    messages.success(request, 'Your table has been booked!')
                    return redirect('book_table')

                except IntegrityError:
                    messages.error(
                        request,
                        'Sorry, that time slot is already booked. Please choose another date or time.'
                    )

        # Newsletter form submitted
        elif 'submit_newsletter' in request.POST:
            booking_form = BookingForm()
            newsletter_form = NewsletterSignupForm(request.POST)

            if newsletter_form.is_valid():
                try:
                    newsletter_form.save()
                    messages.success(request, "You've been added to our newsletter!")
                    return redirect('book_table')
                except IntegrityError:
                    messages.error(
                        request,
                        "You're already subscribed to our newsletter!"
                    )

    else:
        booking_form = BookingForm()
        newsletter_form = NewsletterSignupForm()

    return render(
        request,
        'booking/book_table.html',
        {
            'form': booking_form,
            'newsletter_form': newsletter_form,
        }
    )
