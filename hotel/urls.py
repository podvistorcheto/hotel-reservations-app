from django.urls import path
from . import views


urlpatterns = [
    path('one/', views.test_one, name='page-one'),
    path('two/', views.test_two, name='page-two'),
]