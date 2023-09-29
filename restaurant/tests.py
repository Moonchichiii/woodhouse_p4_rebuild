from django.test import TestCase
from django import forms
from django.forms import ModelForm

from .froms import BookingsForm 
from .models import Bookings

from datetime import datetime, timedelta

# Create your tests here.


class BookingsFormTest(TestCase):
    
    def test_maximum_number_of_guests(self):

        Bookings.objects.create(

            number_of_guests=15,
            date=datetime.today(),
            time= '17:00',
            first_name= 'eva',
            last_name= 'nilsson',
            address= '560 street',
            email='eva.n@gmail.com',
            phone_number= '23134124124'
            
            )


    form_data = {
            'number_of_guests': 15,
            'date': datetime.today(),
            'time' :'17:00',
            'first_name': 'eva',
            'last_name': 'nilsson',
            'address' : '560 street',
            'email' :'eva.n@gmail.com',
            'phone_number' :'23134124124',
    }

    form = BookingsForm(data=form_data)
    self.assertFalse(form.is_valid())
    self.assertEqual(form.errors['__all__'], ['Sorry fully booked! Please choose another time or date.'])
