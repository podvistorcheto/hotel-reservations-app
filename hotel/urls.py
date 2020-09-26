from django.urls import path
from . import views
from .views import RoomList, BookingList, BookingView


urlpatterns = [
    path('', views.test_one, name='page-one'),
    path('gallery/', views.go_to_gallery, name='gallery-page'),
    path('home/', views.test_two, name='page-two'),
    path('rooms/', RoomList.as_view(), name='room-list'),
    path('reserve/', BookingView.as_view(), name='booking-view'),
    path('bookings/', BookingList.as_view(), name='booking-list'),
]