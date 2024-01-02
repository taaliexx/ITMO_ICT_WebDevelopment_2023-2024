## Лабораторная работа №3 "Реализация серверной части на django rest. Документирование API."
### Вариант 1. Отель
Создать программную систему, предназначенную для администратора гостиницы. Такая система должна обеспечивать хранение сведений об имеющихся в гостинице номерах, о проживающих в гостинице клиентах и о служащих, убирающихся в номерах. Количество номеров в гостинице известно, и имеются номера трех типов: одноместный, двухместный и трехместный, отличающиеся стоимостью проживания в сутки. В каждом номере есть телефон. 
* О каждом проживающем должна храниться следующая информация: номер паспорта, фамилия, имя, отчество, город, из которого он прибыл, дата поселения в гостинице, выделенный гостиничный номер.
* О служащих гостиницы должна быть известна информация следующего содержания: фамилия, имя, отчество, где (этаж) и когда (день недели) он убирает. Служащий гостиницы убирает все номера на одном этаже в определенные дни недели, при этом в разные дни он может убирать разные этажи.

Работа с системой предполагает получение следующей информации:

* клиентах, проживавших в заданном номере, в заданный период времени;
* количестве клиентов, прибывших из заданного города,
* о том, кто из служащих убирал номер указанного клиента в заданный день недели,
* сколько в гостинице свободных номеров;
* список клиентов с указанием места жительства, которые проживали в те же дни, что и заданный клиент, в определенный период времени.

Администратор должен иметь возможность выполнить следующие операции:

* принять на работу или уволить служащего гостиницы;
* изменить расписание работы служащего;
* поселить или выселить клиента.

Необходимо предусмотреть также возможность автоматической выдачи отчета о работе гостиницы за указанный квартал текущего года. Такой отчет должен содержать следующие сведения:

* число клиентов за указанный период в каждом номере;
* количество номеров не каждом этаже;
* общая сумма дохода за каждый номер;
* суммарный доход по всей гостинице.

### Модели БД

``` python
from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True)
    passport = models.CharField(max_length=15)
    from_city = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Floor(models.Model):
    floor = models.PositiveIntegerField()

    def __str__(self):
        return f'Floor {self.floor}'


class Room(models.Model):
    ROOM_CATEGORIES = (
        ('SINGLE', 'Single Room'),
        ('DOUBLE', 'Double Room'),
        ('TRIPLE', 'Triple Room'),
    )
    number = models.IntegerField()
    category = models.CharField(max_length=6, choices=ROOM_CATEGORIES)
    cost = models.IntegerField()
    phone = models.CharField(max_length=15)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.number} {self.category} room'


class Bookings(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    check_in_done = models.BooleanField(default=False, null=True, blank=True)
    check_out_done = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f'{self.user} booked {self.room} from {self.check_in} to {self.check_out}'


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class EmployeeSchedule(models.Model):
    DAYS_OF_WEEK = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    work_day = models.CharField(max_length=3, choices=DAYS_OF_WEEK)

    def __str__(self):
        return f"{self.employee} cleans {self.floor} on {self.work_day}s"


class RoomCleaningSchedule(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    employee = models.ForeignKey(EmployeeSchedule, on_delete=models.CASCADE)
    work_date = models.DateField()

    def __str__(self):
        return f"{self.employee} - {self.work_date}"

```