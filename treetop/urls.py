"""treetop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from restaurant.views import index, booking_template, booking_confirmation,cancel_booking, cancelled_confirmation , contactus


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('restaurant/', booking_template, name='bookings'),
    path('restaurant/', index, name='bookings'),
    path('confirmation/<int:booking_id>/', booking_confirmation, name='booking_confirmation'),
    
    path('cancel/', cancel_booking, name='cancel_booking'),
    path('cancelled_confirmation/', cancelled_confirmation, name='cancelled_confirmation'),
    
    path('return/', index, name='index'),

    path('contact/', contactus, name='contactus'),
    
]
