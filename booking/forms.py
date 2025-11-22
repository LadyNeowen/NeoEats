'''
Forms for the Booking app.

Includes:
- BookingForm: Creates and validates table reservations.
- NewsletterSignupForm: Collects newsletter subscription emails.
'''

from django import forms
from .models import Booking, NewsletterSignup
import datetime


class BookingForm(forms.ModelForm):
    '''Form used to submit a table booking.'''

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
        '''Validate opening hours and closed days.'''
        cleaned_data = super().clean()

        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if not date or not time:
            return cleaned_data

        weekday = date.weekday()  # Monday = 0

        # Closed on Mondays
        if weekday == 0:
            raise forms.ValidationError('We are closed on Mondays. Please choose another day.')

        # Opening hours by day
        if weekday in [1, 2, 3]:  # Tue–Thu
            start = datetime.time(16, 0)
            end = datetime.time(21, 0)
        elif weekday in [4, 5]:  # Fri–Sat
            start = datetime.time(16, 0)
            end = datetime.time(23, 0)
        else:  # Sunday
            start = datetime.time(16, 0)
            end = datetime.time(21, 0)

        if not (start <= time <= end):
            raise forms.ValidationError(
                f'Booking time must be between {start.strftime("%H:%M")} and {end.strftime("%H:%M")}.'
            )

        return cleaned_data


class NewsletterSignupForm(forms.ModelForm):
    '''Form for newsletter signup.'''

    class Meta:
        model = NewsletterSignup
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
                'class': 'form-control',
            })
        }
