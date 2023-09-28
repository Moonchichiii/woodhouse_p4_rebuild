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
    context = {
        'cancel_form': form
    }
    return render(request, 'restaurant/cancelled.html', context)



def cancel_confirmation(request, booking_id):
    if request.method == 'POST':
        form = CancelBookingForm(request.POST)
        if form.is_valid():
            booking_id = form.cleaned_data['booking_id']           
            try:
                cancel = Bookings.objects.get(id=booking_id)
                cancel.delete()
                messages.success(request, 'Your booking is cancelled.')
                return redirect('cancel_confirmation', booking_id=booking_id)  
            
            except Bookings.DoesNotExist:
                    messages.error(request,"Booking 'ID' not found, try again!")  
        cancelled = get_object_or_404(Bookings, id=booking_id)
        return render(request, 'restaurant/confirm.html', {'cancel_confirmation': cancelled})
