import datetime

# from django.utils import timezone
from hotel.models import Room, Bookings


def check_availability(room, check_in, check_out):
    if check_out <= check_in:
        return False

    # now = timezone.now()
    # if check_in < now:
    #     return False

    avail_list = []
    bookings_list = Bookings.objects.filter(room=room)
    for booking in bookings_list:
        if booking.check_in > check_out or booking.check_out < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)
