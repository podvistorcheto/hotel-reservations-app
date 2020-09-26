from django.urls import path
from . import views
from .views import RoomList, BookingList, BookingView


urlpatterns = [
    path('bookings/', BookingList.as_view(), name='hotel-bookings'),
]