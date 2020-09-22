from django.urls import path
from . import views
from .views import RoomList, BookingList, BookingView


urlpatterns = [
    path('', views.test_one, name='page-one'),
    path('one/', views.test_two, name='page-two'),
    path('roomlist/', RoomList.as_view(), name='room-list'),
    path('bookinglist/', BookingList.as_view(), name='booking-list'),
    path('reserve/', BookingView.as_view(), name='booking-view'),
]