from django.urls import path
from . import views
from .views import (
    UnitsListView,
    UnitsDetailView,
    RsvsList,
    RsvsView, Pics,
    RsvsDetailsView,
    RsvsUpdateView,
    RsvsDeleteView
)

urlpatterns = [
    path('', UnitsListView.as_view(), name='rooms'),
    path('room/<category>', UnitsDetailView.as_view(), name='RoomDetailView'),
    path('gallery/', Pics.as_view(), name='gallery'),
    path('reserve/',  RsvsView.as_view(), name='reserve'),
    path('bookings/', RsvsList.as_view(), name='bookings'),
    path('bookings/<int:pk>/',
        RsvsDetailsView.as_view(), name='booking-details'),
    path('bookings/<int:pk>/update/',
        RsvsUpdateView.as_view(), name='booking-update'),
    path('bookings/<int:pk>/delete/',
        RsvsDeleteView.as_view(), name='booking-delete'),
]