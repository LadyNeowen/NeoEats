from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookingForm, NewsletterSignupForm
from .models import Booking


@login_required
def book_table(request):
    """
    Display and process the booking form and newsletter signup form.
    Bookings are stored against the logged in user.
    """
    booking_form = BookingForm()
    newsletter_form = NewsletterSignupForm()

    if request.method == "POST":

        # Booking form submitted
        if "submit_booking" in request.POST:
            booking_form = BookingForm(request.POST)
            newsletter_form = NewsletterSignupForm()

            if booking_form.is_valid():
                booking_date = booking_form.cleaned_data.get("date")

                # Hard stop on Mondays (defensive + test-friendly)
                if booking_date and booking_date.weekday() == 0:
                    messages.error(request, "We are closed on Mondays")
                    return render(
                        request,
                        "booking/book_table.html",
                        {
                            "form": booking_form,
                            "newsletter_form": newsletter_form,
                        },
                    )

                try:
                    booking = booking_form.save(commit=False)
                    booking.user = request.user
                    booking.save()

                    if settings.DEBUG:
                        send_mail(
                            subject="Your NeoEats Booking Confirmation",
                            message=(
                                "Thank you for booking a table at NeoEats!\n\n"
                                "Here are your booking details:\n"
                                f"Name: {booking.name}\n"
                                f"Date: {booking.date}\n"
                                f"Time: {booking.time}\n"
                                f"Guests: {booking.guests}\n\n"
                                "We look forward to seeing you!"
                            ),
                            from_email="neoeats@example.com",
                            recipient_list=[booking.email],
                            fail_silently=False,
                        )

                    messages.success(request, "Your table has been booked!")
                    return redirect("my_bookings")

                except IntegrityError:
                    messages.error(
                        request,
                        (
                            "Sorry, that time slot is already booked. "
                            "Please choose another date or time."
                        ),
                    )

        # Newsletter form submitted
        elif "submit_newsletter" in request.POST:
            booking_form = BookingForm()
            newsletter_form = NewsletterSignupForm(request.POST)

            if newsletter_form.is_valid():
                try:
                    newsletter_form.save()
                    messages.success(request, "You've been added to our newsletter!")
                    return redirect("book_table")
                except IntegrityError:
                    messages.error(
                        request, "You're already subscribed to our newsletter!"
                    )

    return render(
        request,
        "booking/book_table.html",
        {
            "form": booking_form,
            "newsletter_form": newsletter_form,
        },
    )


@login_required
def my_bookings(request):
    """
    Display the logged in user's bookings.
    """
    bookings = Booking.objects.filter(user=request.user).order_by("-date", "-time")
    return render(request, "booking/my_bookings.html", {"bookings": bookings})


@login_required
def edit_booking(request, booking_id):
    """
    Allow the user to edit one of their bookings.
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)

        if form.is_valid():
            booking_date = form.cleaned_data.get("date")

            if booking_date and booking_date.weekday() == 0:
                messages.error(request, "We are closed on Mondays")
            else:
                try:
                    form.save()
                    messages.success(request, "Your booking has been updated!")
                    return redirect("my_bookings")
                except IntegrityError:
                    messages.error(
                        request,
                        (
                            "Sorry, that time slot is already booked. "
                            "Please choose another date or time."
                        ),
                    )
    else:
        form = BookingForm(instance=booking)

    return render(
        request, "booking/edit_booking.html", {"form": form, "booking": booking}
    )


@login_required
def cancel_booking(request, booking_id):
    """
    Allow the user to cancel (delete) one of their bookings.
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == "POST":
        booking.status = "cancelled"
        booking.save(update_fields=["status"])
        messages.success(request, "Your booking has been cancelled.")
        return redirect("my_bookings")

    return render(request, "booking/cancel_booking.html", {"booking": booking})
