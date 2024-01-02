from django.db.models import ExpressionWrapper, F, fields, Func

from .models import Room, Bookings
from datetime import datetime, timedelta


def get_available_rooms(check_in_date, check_out_date):
    check_in_date = datetime.strptime(check_in_date, '%Y-%m-%d').date()
    check_out_date = datetime.strptime(check_out_date, '%Y-%m-%d').date()

    # Получение всех комнат
    all_rooms = Room.objects.all()

    # Получение всех бронирований в заданный период
    booked_rooms = Bookings.objects.filter(
        check_in__lte=check_out_date,
        check_out__gte=check_in_date
    ).values_list('room_id', flat=True)

    # Получение свободных комнат
    available_rooms = all_rooms.exclude(id__in=booked_rooms)

    return available_rooms.values()

