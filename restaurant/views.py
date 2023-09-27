from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django import forms
from restaurant.forms import BookingsForm
from restaurant.models import Bookings


# Create your views here.

def index(request):
    key = settings.GOOGLE_API_KEY
    form = BookingsForm()
    context = {
        'key': key,
        'form': form
    }
    return render(request, 'restaurant/index.html', context)


def booking_template(request):
    if request.method == 'POST':
        form = BookingsForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingsForm()        

    context = {
        'form': form
    }
    return render(request, 'restaurant/index.html', context)


def booking_confirmation(request, booking_id):
    confirmation = get_object_or_404(Bookings, id=booking_id)
    return render(request, 'restaurant/confirm.html', {'booking': confirmation})