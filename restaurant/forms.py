from django import forms
from django.db import models
from .models import Bookings

class BookingsForm(forms.ModelForm):
   date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))    
   class Meta:
        model = Bookings
        fields = [
            'number_of_guests',
            'date',
            'time',
            'first_name',
            'last_name',
            'address',
            'email',
            'phone_number',
            'comment']
    

   def clean(self):
    cleaned_data = super().clean()
    date = cleaned_data.get("date")
    time = cleaned_data.get("time")
    number_of_guests = cleaned_data.get("number_of_guests")

    max_guests = 20 


    existing_bookings_count = Bookings.objects.filter(date=date, time=time).aggregate(total_guests=models.Sum('number_of_guests'))['total_guests'] or 0
    
    if existing_bookings_count + number_of_guests > max_guests:
        raise forms.ValidationError("Sorry fully booked! Please choose time or date.")

class CancelBookingForm(forms.Form):
    booking_id = forms.IntegerField(label='Booking ID')
            