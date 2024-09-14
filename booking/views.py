from django.shortcuts import render
from booking.models import Room, Booking

# Create your views here.

def rooms_list(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
    }
    return render(request, 'booking/rooms_list.html', context)