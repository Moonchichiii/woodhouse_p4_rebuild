from django.db import models
from django.utils import timezone
from datetime import time

class MenuChangeAndPrices(models.Model):

    STARTER = 'Starter'
    MAIN_COURSE = 'Main Couse'
    DESSERT = 'Dessert'


    CATEGORY_OPTIONS = [
        (STARTER, ''),
        (MAIN_COURSE, 'Main Course'),
        (DESSERT, 'Dessert'),
    ]
    TIME_OPTIONS = [
    ('17:00', '5:00 PM'),
    ('17:30', '5:30 PM'),
    ('18:00', '6:00 PM'),
    ('18:30', '6:30 PM'),
    ('19:00', '7:00 PM'),
    ('19:30', '7:30 PM'),
    ('20:00', '8:00 PM'),
    ('20:30', '8:30 PM'),
    ('21:00', '9:00 PM'),
    ('21:30', '9:30 PM'),
    ('22:00', '10:00 PM'),
    ]
    
    number_of_guests = models.PositiveIntegerField(choices=GUEST_OPTIONS)
    date = models.DateField()
    time = models.CharField(max_length=5, choices=TIME_OPTIONS)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=80, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=180,)
    catecory = models.CharField(max_length=80, choices=CATEGORY_OPTIONS)
    price = models.DecimalField(max_digits=6, decimal_places=2)
   
   

# Create your models here.
class Bookings(models.Model):    
    GUEST_OPTIONS = [        
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10'),
        ]


    TIME_OPTIONS = [
    ('17:00', '5:00 PM'),
    ('17:30', '5:30 PM'),
    ('18:00', '6:00 PM'),
    ('18:30', '6:30 PM'),
    ('19:00', '7:00 PM'),
    ('19:30', '7:30 PM'),
    ('20:00', '8:00 PM'),
    ('20:30', '8:30 PM'),
    ('21:00', '9:00 PM'),
    ('21:30', '9:30 PM'),
    ('22:00', '10:00 PM'),
    ]
    
    number_of_guests = models.PositiveIntegerField(choices=GUEST_OPTIONS)
    date = models.DateField()
    time = models.CharField(max_length=5, choices=TIME_OPTIONS)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=80, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False) 
    comment = models.TextField(max_length=20,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.date} {self.time}"
