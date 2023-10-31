* Функция для проверки доступности номера на конкретные даты
* Функция для названия и url категории номера
```python title="avaliability.py"
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
```

```python title="get_room_cat_url_list.py"
from django.urls import reverse
from hotel.models import Room


def get_room_cat_url_list():
    room = Room.objects.all()[0]
    room_cat_url_list = []
    room_categories = dict(room.ROOM_CATEGORIES)

    for category in room_categories:
        room_category = room_categories.get(category)
        room_url = reverse('hotel:RoomDetailView', kwargs={'category': category})
        room_cat_url_list.append((room_category, room_url))

    return room_cat_url_list
```