from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    uesr = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    loyalty_points = models.IntegerField(default=0)
    membership_level = models.CharField(max_length=20, choice=[
        ('bronze', 'Bronze'),
        ('silver', 'Silver'),
        ('gold', 'Gold')
    ], default='bronze')

    def __str__(self):
        return self.user.username

