from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class CarOwner(AbstractUser):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField(blank=True, null=True)
    cars = models.ManyToManyField('Car', through='Ownership', blank=True, null=True)

    passport = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Car(BaseModel):
    license_plate = models.CharField(max_length=15)
    car_brand = models.CharField(max_length=20)
    car_model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, blank=True, null=True)
    owners = models.ManyToManyField('CarOwner', through='Ownership', blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.car_brand, self.car_model)


class Ownership(BaseModel):
    car_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE, blank=True, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.car_owner, self.car)


class DriversLicense(BaseModel):
    car_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10)
    issued_date = models.DateField()

    def __str__(self):
        return "{}".format(self.license_number)
