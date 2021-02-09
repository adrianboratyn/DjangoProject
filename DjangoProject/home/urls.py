from django.urls import path
from .views import TripsListView, TripsDetailView, AboutView
from . import views
from .views import HomeView, ExchangeRatesView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('oferty/', TripsListView.as_view(), name='wycieczki'),
    path('oferty/<int:pk>/', TripsDetailView.as_view(), name='trips-detail'),
    path('oferty/<int:pk>/succes', views.reservation, name='reservation'),
    path('waluty/', ExchangeRatesView.as_view(), name="exchangerates"),
    path('kontakt/', views.contact, name="contact"),
    path('onas/', AboutView.as_view(), name="about"),
]
