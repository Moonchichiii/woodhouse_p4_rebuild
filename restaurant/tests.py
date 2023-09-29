from django.test import TestCase
from django import forms
from django.urls import reverse
from django.forms import ModelForm
from .forms import BookingsForm, CancelBookingForm
from .models import Bookings
from datetime import datetime
    
# Create your tests here.

#  Views Testing

class landing_page(TestCase):
    def test_landing_page(self):
        response = self.client.get('') 
        self.assertEqual(response.status_code, 200)

class ViewTest(TestCase):
    def test_views_loading(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('booking_form', response.context)
        self.assertIn('cancel_form', response.context)
        self.assertIn('starters', response.context)
        self.assertIn('main_course', response.context)
        self.assertIn('desserts', response.context)
        self.assertIn('contactus', response.context)






# forms tests

def test_contact_us(self):
    response = self.client.post('/contactus', {'email': 'test@example.com'})
    self.assertEqual(response.status_code, 200)

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


# models tests 

def test_model(self):
        instance = Bookings.objects.get(first_name='Eva', last_name='Nilsson')
        self.assertEqual(instance.first_name, 'Eva')
        self.assertEqual(instance.last_name, 'Nilsson')
        self.assertEqual(instance.address, 'bagargatan 10')
        self.assertEqual(instance.email, 'eva.nilsson@gmail.com')
        self.assertEqual(instance.phone_number, '546254375')












