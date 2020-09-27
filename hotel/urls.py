from django.urls import path
from . import views
from .views import RoomList, BookingList, BookingView, Gallery


urlpatterns = [
    path('', RoomList.as_view(), name='rooms'),
    path('gallery/', Gallery.as_view(), name='gallery'),
    path('bookings/', BookingList.as_view(), name='bookings'),
    path('reserve/', BookingView.as_view(), name='reserve'),
]