
from django.shortcuts import render, redirect
from .models import Trip,Contact
from .forms import ReservationForm,ContactForm
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

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

def Contact(request):
    if request.method == 'POST':
        c_form = ContactForm(request.POST)
        if c_form.is_valid():
            c_form.save()
            messages.success(request, f'Zapytanie zostało wysłane pomyslnie')
            return redirect('home')

    else:
        c_form = ContactForm()

    return render(request, 'home/contact.html', {'form': c_form})




class HomeView(TemplateView):
    template_name = "home/home.html"

class ExchangeRatesView(TemplateView):
    template_name = "home/exchangerates.html"
    
class ContactView(TemplateView):
    template_name = "home/contact.html"    
