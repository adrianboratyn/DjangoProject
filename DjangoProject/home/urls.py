from django.contrib import admin
from django.urls import path
from .views import TripsListView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('oferty/', TripsListView.as_view(), name='wycieczki'),
]