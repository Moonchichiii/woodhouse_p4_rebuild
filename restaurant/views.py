from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.conf import settings
from django import forms
from django.contrib import messages
from restaurant.forms import BookingsForm, CancelBookingForm, ContactForm
from restaurant.models import Bookings, MenuChangeAndPrices
import requests


# Create your views here.

def index(request):

    key = settings.GOOGLE_API_KEY
    booking_form = BookingsForm()
    cancel_form = CancelBookingForm()
    starters = MenuChangeAndPrices.objects.filter(category=MenuChangeAndPrices.STARTER)
    main_course = MenuChangeAndPrices.objects.filter(category=MenuChangeAndPrices.MAIN_COURSE)
    desserts = MenuChangeAndPrices.objects.filter(category=MenuChangeAndPrices.DESSERT)
    contactus = ContactForm()
    context = {
        'key': key,
        'booking_form': booking_form,
        'cancel_form': cancel_form,
        'starters': starters,
        'main_course': main_course,
        'desserts': desserts,
        'contactusform': contactus

    }
    return render(request, 'restaurant/index.html', context)


def booking_template(request):
    if request.method == 'POST':
        form = BookingsForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return redirect('booking_confirmation', booking_id=booking.id)

        else:
            messages.error(request, "Sorry fully booked! Please choose another time or date.")
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


def response_message(user_email):

    mailgun_domain = settings.ANYMAIL['MAILGUN_SENDER_DOMAIN']
    mailgun_api_key = settings.ANYMAIL['MAILGUN_API_KEY']
    mailgun_from_email = settings.DEFAULT_FROM_EMAIL

    return requests.post(
       f"https://api.mailgun.net/v3/{mailgun_domain}/messages",
        auth=("api", mailgun_api_key),
        data={"from": f"Excited User <{mailgun_from_email}>",
              "to": [user_email],
              "subject": "Thank you for contacting us!",
              "text": "We received your message and will get back to you, as soon as possible."})


def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            response_message(user_email)
            messages.success(request, 'Message sent...')
            return render(request, 'restaurant/index.html')
    else:
        form = ContactForm()
    return render(request, 'modal_contactus.html', {'contactusform': form})