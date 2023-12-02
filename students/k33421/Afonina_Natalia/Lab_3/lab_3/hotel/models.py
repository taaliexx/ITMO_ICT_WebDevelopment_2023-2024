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
    cost = models.DecimalField(max_digits=10, decimal_places=2)
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
