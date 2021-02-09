from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """Klasa formularza rejestracji.

    Args:
        UserCreationForm 
    """
    email = forms.EmailField()

    class Meta:
        """Przypisanie modelu użytkownika i potrzebnych pól.
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    """Klasa formularza aktualizacji modelu użytkownika.

    Args:
        forms (ModelForm)
    """
    email = forms.EmailField()

    class Meta:
        """Przypisanie modelu użytkownika i potrzebnych pól do aktualizacji.
        """
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """Klasa formularza aktualizacji profilu użytkownika.

    Args:
        forms (ModelForm)
    """
    class Meta:
        """Przypisanie profilu użytkownika i potrzebnych pól do aktualizacji.
        """
        model = Profile
        fields = ['image']