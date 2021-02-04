from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Trip(models.Model):
    title = models.CharField(max_length=100)
    Hotel = models.TextField(blank=True)
    description = models.TextField(blank=True)
    duration = models.TextField(blank=True)
    deadline1 = models.DateField(auto_now_add=False, blank=True)
    deadline2 = models.DateField(auto_now_add=False, blank=True)
    deadline3 = models.DateField(auto_now_add=False, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=0, default=5)
    price = models.DecimalField(max_digits=15000, decimal_places=2, default=0)
    main_image = models.ImageField(upload_to='trips_pics', blank=True)
    image_one = models.ImageField(upload_to='trips_pics', blank=True)
    image_two = models.ImageField(upload_to='trips_pics', blank=True)
    image_three = models.ImageField(upload_to='trips_pics', blank=True)
    image_four = models.ImageField(upload_to='trips_pics', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class Reservation(models.Model):
    user = models.TextField(blank=True)
    trip = models.TextField(blank=True)
    day = models.TextField(blank=True)
    adults = models.DecimalField(max_digits=2, decimal_places=0, default=1)
    kids = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    phone = models.DecimalField(max_digits=9, decimal_places=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    guide = models.BooleanField(default=0)
    room = models.BooleanField(default=0)


