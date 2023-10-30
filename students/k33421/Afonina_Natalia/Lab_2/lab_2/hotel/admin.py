from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Room, Hotel, Bookings, Review, Confirmation

admin.site.register(Room)
admin.site.register(Hotel)
admin.site.register(Bookings)
admin.site.register(Review)
admin.site.register(Confirmation)



