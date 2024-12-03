from django.contrib import admin
from .models import Table, Reservation

# Register your models here.

admin.site.register(table)
admin.site.register(Reservation)