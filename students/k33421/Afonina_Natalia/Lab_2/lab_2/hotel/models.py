from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, AbstractUser
from django.core.exceptions import PermissionDenied
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse, reverse_lazy


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Room(models.Model):
    ROOM_CATEGORIES = (
        ('SINGLE', 'Single Room'),
        ('DOUBLE', 'Double Room'),
        ('FAMILY', 'Family Room'),
        ('DELUXE', 'Deluxe Room'),
        ('SUIT', 'Suit'),
    )
    number = models.IntegerField()
    category = models.CharField(max_length=6, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    amenities = models.TextField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.number} {self.category} room'


class Bookings(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'

    def get_room_category(self):
        room_categories = dict(self.room.ROOM_CATEGORIES)
        room_category = room_categories.get(self.room.category)
        return room_category

    def get_cancel_booking_url(self):
        return reverse_lazy('hotel:CancelBookingView', args=[self.pk, ])

    def edit_booking(self):
        return reverse_lazy('hotel:EditBookingView', args=[self.pk, ])

    def create_review(self, rating, text):
        review = Review.objects.create(user=self.user, room=self.room, rating=rating, text=text)
        return review


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=5, choices=[(i, i) for i in range(1, 11)])
    text = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking = models.ForeignKey(Bookings, on_delete=models.CASCADE)

    def __str__(self):
        return f'Review by {self.user} for Room'


class Confirmation(models.Model):
    booking = models.OneToOneField(Bookings, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)
    confirmed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    confirmation_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.confirmed_by and not self.confirmed_by.is_staff:
            raise PermissionDenied("Only staff members can confirm bookings.")
        super(Confirmation, self).save(*args, **kwargs)
