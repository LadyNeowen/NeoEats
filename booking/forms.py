from django import forms
from .models import Booking
import datetime

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'date', 'time', 'guests', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'guests': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        time = cleaned_data.get("time")

        if not date or not time:
            return cleaned_data

        weekday = date.weekday()  
        # Monday = 0, Tuesday = 1, ..., Sunday = 6

        # -------------------------
        # CLOSED ON MONDAYS
        # -------------------------
        if weekday == 0:
            raise forms.ValidationError(
                "We are closed on Mondays. Please choose another day."
            )

        # -------------------------
        # OPENING HOURS
        # -------------------------
        opening_time = datetime.time(16, 0)  # 16:00
        closing_time = datetime.time(21, 0)  # default closing

        # Friday & Saturday → open until 23:00
        if weekday in (4, 5):  # Fri=4, Sat=5
            closing_time = datetime.time(23, 0)

        # Validate time range
        if not (opening_time <= time <= closing_time):
            raise forms.ValidationError(
                f"Our opening hours are {opening_time.strftime('%H:%M')}–{closing_time.strftime('%H:%M')} on this day."
            )

        # -------------------------
        # CHECK FOR DOUBLE BOOKINGS
        # -------------------------
        if Booking.objects.filter(date=date, time=time).exists():
            raise forms.ValidationError(
                "This time slot is already booked. Please choose another."
            )

        return cleaned_data
