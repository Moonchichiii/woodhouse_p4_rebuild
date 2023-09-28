from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django import forms
from django.contrib import messages
from restaurant.forms import BookingsForm, CancelBookingForm
from restaurant.models import Bookings


# Create your views here.

def index(request):
    key = settings.GOOGLE_API_KEY
    booking_form = BookingsForm()
    cancel_form = CancelBookingForm()
    context = {
        'key': key,
        'booking_form': booking_form,
        'cancel_form': cancel_form,
    }
    return render(request, 'restaurant/index.html', context)


def booking_template(request):
    if request.method == 'POST':
        form = BookingsForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return redirect('booking_confirmation', booking_id=booking.id)
    
        else:
            messages.error(request,"Sorry fully booked! Please choose time or date.")                    
    else:
        form = BookingsForm()        

    context = {
        'booking_form': form
    }
    return render(request, 'restaurant/index.html', context)


def booking_confirmation(request, booking_id):
    confirmation = get_object_or_404(Bookings, id=booking_id)
    return render(request, 'restaurant/confirm.html', {'booking': confirmation})


def cancel_booking(request):
    if request.method == 'POST':
        cancel_form = CancelBookingForm(request.POST)
        if cancel_form.is_valid():
            booking_id = cancel_form.cleaned_data['booking_id']
            try:
                cancel = Bookings.objects.get(id=booking_id)
                cancel.delete()
                messages.success(request, 'Your booking has been successfully cancelled!')
                return redirect('cancelled_confirmation')
            except Bookings.DoesNotExist:
                cancelled_confirmation(request)
                messages.error(request, "Booking 'ID' not found, try again!")
    else:
        cancel_form = CancelBookingForm()

    return render(request, 'restaurant/cancelled.html', {'cancel_form': cancel_form})


def cancelled_confirmation(request):
    return render(request, 'restaurant/cancelled.html')
  

       