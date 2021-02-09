from django.contrib import admin
from .models import Trip, Reservation, Contact

# rejestracja modeli w panelu admina
admin.site.register(Trip)
admin.site.register(Reservation)
admin.site.register(Contact)
