from django import forms
from .models import Reservation, Contact


class ReservationForm(forms.ModelForm):
    """ Klasa prezentująca formularz rezerwacji

    Args:
        forms (ModelForm): 
    """
    class Meta:
        """Przypisanie modelu rezerwacji i potrzebnych pól
        """
        model = Reservation
        fields = ['user', 'trip', 'day', 'adults', 'kids', 'phone', 'guide', 'room', 'price']


class ContactForm(forms.ModelForm):
    """Klasa prezentująca formularz kontaktu

    Args:
        forms (ModelForm): 
    """
    class Meta:
        """Przypisanie modelu kontaktu i potrzebnych pól
        """
        model = Contact
        fields = ['NameAndLastName', 'Email', 'Telephone', 'Thema', 'Content']
