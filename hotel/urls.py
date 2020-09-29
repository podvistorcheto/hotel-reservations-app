from django.urls import path
from . import views
from .views import (
    RoomList,
    BookingList,
    BookingView, Gallery,
    BookingDetailsView,
    BookingUpdateView,
    BookingDeleteView
)

urlpatterns = [
    path('', RoomList.as_view(), name='rooms'),

    path('gallery/', Gallery.as_view(), name='gallery'),
    path('reserve/', BookingView.as_view(), name='reserve'),
    path('bookings/', BookingList.as_view(), name='bookings'),
    path('bookings/<int:pk>/',
        BookingDetailsView.as_view(), name='booking-details'),
    path('bookings/<int:pk>/update/',
        BookingUpdateView.as_view(), name='booking-update'),
    path('bookings/<int:pk>/delete/',
        BookingDeleteView.as_view(), name='booking-delete'),
]