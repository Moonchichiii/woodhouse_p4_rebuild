from django.contrib import admin
from restaurant.models import Bookings

# Register your models here.
@admin.register(Bookings)

class BookingsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date', 'time', 'number_of_guests', 'phone_number', 'email','id')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('date', 'time', 'number_of_guests' ,'id')
