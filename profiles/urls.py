from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('userpage/', auth_views.LoginView.as_view(), name='userpage'),
]