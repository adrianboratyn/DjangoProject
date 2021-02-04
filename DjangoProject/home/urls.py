from django.contrib import admin
from django.urls import path
from .views import TripsListView, TripsDetailView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('oferty/', TripsListView.as_view(), name='wycieczki'),
    path('oferty/<int:pk>/', TripsDetailView.as_view(), name='trips-detail'),
    path('oferty/<int:pk>/succes', views.reservation, name='reservation'),

]