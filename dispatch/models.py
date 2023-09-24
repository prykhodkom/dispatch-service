from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Truck(models.Model):
    type = models.CharField(max_length=255)
    length = models.IntegerField()
    max_weight = models.IntegerField()

    class Meta:
        ordering = ["type"]

    def __str__(self):
        return f"{self.type} with length: {self.length}' and max weight: {self.max_weight} lbs"


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Driver(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    home_location = models.CharField(max_length=255)
    worker = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="drivers")
    type_of_truck = models.ForeignKey(Truck, on_delete=models.CASCADE)

    class Meta:
        ordering = ("first_name", "last_name")
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self):
        return f"{self.first_name} {self.last_name}, phone# {self.phone_number}"
