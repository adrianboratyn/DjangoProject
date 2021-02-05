from django import forms
from .models import Reservation,Contact


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'trip', 'day', 'adults', 'kids', 'phone', 'guide', 'room', 'price']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['NameAndLastName', 'Email', 'Telephone', 'Thema', 'Content']

  