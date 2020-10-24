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
    path('', UnitsListView.as_view(), name='test'),
]