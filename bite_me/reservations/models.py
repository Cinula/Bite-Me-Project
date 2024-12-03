from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Table(models.Model):
    table_number = models.IntegerField(unique = True)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number} (Capacity:{self.capacity})"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.IntegerField()
    status = models.CharField(max_length = 20, 
    choice=[
        ('pending','Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
        ], default='pending')
    special_requests = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reservation for {self.user.username} on {self.date} at {self.time}"