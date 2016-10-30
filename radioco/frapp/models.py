from django.db import models
from solo.models import SingletonModel


class Station(SingletonModel):
    name = models.CharField(max_length=256)
    display_name = models.CharField(max_length=256)
    city = models.CharField(max_length=128)
    description = models.TextField(max_length=256)


class Studio(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    city = models.CharField(max_length=128)
    street = models.CharField(max_length=256)
    number = models.PositiveSmallIntegerField()
    zip = models.DecimalField(max_digits=5, decimal_places=0)
    open_from = models.TimeField()
    open_to = models.TimeField()
