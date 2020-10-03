from django.db import models
from solo.models import SingletonModel


class Station(SingletonModel):
    name = models.CharField(max_length=256)
    display_name = models.CharField(max_length=256)
    city = models.CharField(max_length=128)
    description = models.TextField(max_length=256)
    website = models.URLField()
    logo_url = models.URLField()


class Studio(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    city = models.CharField(max_length=128)
    street = models.CharField(max_length=256)
    number = models.PositiveSmallIntegerField()
    zip = models.DecimalField(max_digits=5, decimal_places=0)
    email = models.EmailField()
    phone = models.CharField(max_length=32)
    location_latitude = models.DecimalField(max_digits=10, decimal_places=7)
    location_longitude = models.DecimalField(max_digits=10, decimal_places=7)
    open_from = models.TimeField()
    open_to = models.TimeField()

    @property
    def location(self):
        return (self.location_latitude, self.location_longitude)

    def __str__(self):
        return "{} - {} {}".format(self.city, self.street, self.number)


class CableTransmitter(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    frequency = models.DecimalField(max_digits=6, decimal_places=2)
    operator = models.CharField(max_length=128)
    transmission_from = models.TimeField()
    transmission_to = models.TimeField()


class UKWTransmitter(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    frequency = models.DecimalField(max_digits=6, decimal_places=2)
    city = models.CharField(max_length=128)
    operator = models.CharField(max_length=128)
    rds_id = models.CharField(max_length=64)
    location_latitude = models.DecimalField(max_digits=10, decimal_places=7)
    location_longitude = models.DecimalField(max_digits=10, decimal_places=7)
    transmission_power = models.PositiveSmallIntegerField()
    transmission_range = models.PositiveSmallIntegerField()
    transmission_from = models.TimeField()
    transmission_to = models.TimeField()

    @property
    def location(self):
        return (self.location_latitude, self.location_longitude)

    def __str__(self):
        return "{} - {} MHz".format(self.city, self.frequency)


class StreamTransmitter(models.Model):
    CONTENT_TYPE = (
        (1, 'audio/mpeg'),
        (2, 'application/ogg'),
    )

    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    url = models.URLField()
    content_type = models.PositiveSmallIntegerField(choices=CONTENT_TYPE)
    bitrate = models.DecimalField(max_digits=3, decimal_places=0)
    transmission_from = models.TimeField()
    transmission_to = models.TimeField()
