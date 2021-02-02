from django.shortcuts import render
from .models import Trip
from django.views.generic import ListView, DetailView


def home(request):
    return render(request, 'home/home.html')


class TripsListView(ListView):
    model = Trip
    template_name = 'home/trips.html'
    context_object_name = 'trips'
    ordering = ['date_posted']


def wycieczki(request):
    context = {
        'trips': Trip.objects.all()
    }
    return render(request, 'home/trips.html', context)


class TripsDetailView(DetailView):
    model = Trip
    template_name = 'home/trips-detail.html'
