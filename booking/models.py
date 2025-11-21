from django.db import models

# Create your models here.

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('cancelled', 'Cancelled'),
    ]
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    
    date = models.DateField()
    time = models.TimeField()
    
    guests = models.PositiveIntegerField()
    
    notes = models.TextField(blank=True)
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('date', 'time',) # Prevent double bookings at the same date and time
        
    def __str__(self):
        return f"Booking for {self.name} on {self.date} at {self.time}"