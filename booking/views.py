from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import BookingForm
from .models import Booking

def book_table(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            
            # Send confirmation email
            send_mail(
                subject="Your NeoEats Booking Confirmation",
                message=f"""
Thank you for booking a table at NeoEats!

Here are your booking details:
Name: {booking.name}
Date: {booking.date}
Time: {booking.time}
Guests: {booking.guests}

We look forward to seeing you!
""",
                from_email="neoeats@example.com",
                recipient_list=[booking.email],
                fail_silently=False,
            )

            # Success message
            messages.success(request, "Your table has been booked! Check your email for confirmation.")

            return redirect("book_table")
    else:
        form = BookingForm()

    return render(request, "booking/book_table.html", {"form": form})
