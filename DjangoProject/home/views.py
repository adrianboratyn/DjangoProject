from django.shortcuts import render, redirect
from .models import Trip
from .forms import ReservationForm
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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


@login_required
def reservation(request, *args, **kwargs):
    if request.method == 'POST':
        r_form = ReservationForm(request.POST)
        if r_form.is_valid():
            r_form.save()
            messages.success(request, f'Rezerwacja została złożona')
            return redirect('wycieczki')

    else:
        r_form = ReservationForm()

    context = {
        'form': r_form,
        'kwargs': kwargs,
    }
    return render(request, 'home/partials/reservation.html', context)
