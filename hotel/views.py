from django.shortcuts import render, HttpResponse
from .models import Room, Booking
from django.views.generic import ListView, FormView
from .forms import CheckRoomsForm
from hotel.booking_functions.availability import check_availability


def test_one(request):
    return render(request, 'hotel/base.html')


def test_two(request):
    return render(request, 'hotel/about.html', {'title': 'About'})


class RoomList(ListView): 
    model = Room 


class BookingList(ListView): 
    model = Booking 


class BookingView(FormView):
    form_class = CheckRoomsForm
    template_name = 'availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(category=data['room_category'])
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)
        if len(available_rooms)>0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user = self.request.user,
                room = room,
                adults = data['adults'],
                children = data['children'],
                check_in = data['check_in'],
                check_out = data['check_out'],
                specials = ['specials'],
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('These rooms are booked the dates you are looking for.')
