from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Car, CarOwner, DriversLicense, Ownership

admin.site.register(Car)
admin.site.register(CarOwner)
admin.site.register(DriversLicense)
admin.site.register(Ownership)

