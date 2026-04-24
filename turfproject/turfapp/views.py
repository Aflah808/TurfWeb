from django.shortcuts import render
from .models import Booking


def index(request):
    return render(request,'index.html')

def book(request):
    bookings = Booking.objects.all()
    return render(request, 'book.html', {'bookings': bookings})
