'''
Admin configuration for the Booking app.
Registers models for management in Django admin.
'''

from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    '''Admin configuration for Booking objects.'''
    list_display = ('name', 'date', 'time', 'guests', 'status')
    list_filter = ('status', 'date')
    search_fields = ('name', 'email', 'phone')
    ordering = ('date', 'time')
