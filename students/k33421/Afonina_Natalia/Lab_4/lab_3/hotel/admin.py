from .models import *
from django.contrib import admin

admin.site.register(Client)
admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(Bookings)
admin.site.register(Employee)
admin.site.register(EmployeeSchedule)
admin.site.register(RoomCleaningSchedule)
admin.site.register(User)

