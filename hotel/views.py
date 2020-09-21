from django.shortcuts import render, HttpResponse


bookings = [
    {
        'user': 'dsd',
        'room': 'Room 1',
        'content': 'has booked',
        'checkin': 'August 27, 2018',
        'checkout': 'August 29, 2018'
    },
    {
        'user': 'jane doe',
        'room': 'Room 2',
        'content': 'has booked',
        'checkin': 'August 27, 2018',
        'checkout': 'August 29, 2018'
    }
]


def test_one(request):
    context = {
        'bookings': bookings
    }
    return render(request, 'hotel/home.html', context)


def test_two(request):
    return render(request, 'hotel/about.html', {'title': 'About'})
