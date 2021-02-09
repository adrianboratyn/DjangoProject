from django.shortcuts import render, redirect
from .models import Trip
from .forms import ReservationForm, ContactForm
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


class TripsListView(ListView):
    """[summary]

    Args:
        ListView
    """
    model = Trip
    template_name = 'home/trips.html'
    context_object_name = 'trips'
    ordering = ['date_posted']


class TripsDetailView(DetailView):
    model = Trip
    template_name = 'home/trips-detail.html'


@login_required
def reservation(request, *args, **kwargs):
    """Metoda sprawdza czy formularz został wysłany,
     jesli tak to sprawdza jego poprawność,
     zapisuje zmiany oraz przenosi na stronę z wycieczkami.

    Args:
       request, *args, **kwargs

    Returns:
        Strona z wycieczkami w przypadku sukcesu lub
        strona z rezerwacją w przypadku niepowodzenia.
    """
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


def contact(request):
    """Metoda sprawdza czy formularz został wysłany,
     jesli tak to sprawdza jego poprawność,
     zapisuje zmiany oraz przenosi na stronę startową.

    Args:
       request

    Returns:
        Strona startowa w przypadku sukcesu lub
        strona z kontaktem w przypadku niepowodzenia.
    """
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
    """Klasa widoku strony startowej

    Args:
        TemplateView
    """
    template_name = "home/home.html"


class ExchangeRatesView(TemplateView):
    """Klasa widoku strony z kursami walut

    Args:
        TemplateView
    """
    template_name = "home/exchangerates.html"
    

class ContactView(TemplateView):
    """Klasa widoku strony kontaktowej

    Args:
        TemplateView
    """
    template_name = "home/contact.html"  


class AboutView(TemplateView):
    """Klasa widoku strony 'O nas'

    Args:
        TemplateView
    """
    template_name = "home/about.html"  
