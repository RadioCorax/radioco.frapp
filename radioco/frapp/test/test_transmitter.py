import datetime

from decimal import Decimal
from django.test import TestCase
from radioco.frapp.models import (
    CableTransmitter, StreamTransmitter, UKWTransmitter, Station)


class CableTransmitterModelTest(TestCase):

    def setUp(self):
        self.station = Station.objects.create()
        self.cable_transmitter = CableTransmitter.objects.create(
            station=self.station,
            frequency=123.45,
            operator="KabelFritze",
            transmission_from=datetime.time(10, 0, 0),
            transmission_to=datetime.time(20, 0, 0))

    def test_frequency(self):
        self.assertEqual(123.45, self.cable_transmitter.frequency)

    def test_operator(self):
        self.assertEqual("KabelFritze", self.cable_transmitter.operator)

    def test_from(self):
        self.assertEqual(
            datetime.time(10, 0, 0), self.cable_transmitter.transmission_from)

    def test_to(self):
        self.assertEqual(
            datetime.time(20, 0, 0), self.cable_transmitter.transmission_to)

    def test_station(self):
        self.assertEqual(self.station, self.cable_transmitter.station)


class UKWTransmitterModelTest(TestCase):

    def setUp(self):
        self.station = Station.objects.create()
        self.ukw_transmitter = UKWTransmitter.objects.create(
            station=self.station,
            frequency=Decimal('95.9'),
            city="Petersberg",
            operator="Funkturm",
            rds_id="frn",
            location_latitude=Decimal('-33.8688197'),
            location_longitude=Decimal('151.2092955'),
            transmission_power=1500,
            transmission_range=50,
            transmission_from=datetime.time(10, 0, 0),
            transmission_to=datetime.time(20, 0, 0))
        self.ukw_transmitter.clean_fields()

    def test_frequency(self):
        self.assertEqual(95.9, float(self.ukw_transmitter.frequency))

    def test_city(self):
        self.assertEqual("Petersberg", self.ukw_transmitter.city)

    def test_operator(self):
        self.assertEqual("Funkturm", self.ukw_transmitter.operator)

    def test_rds_id(self):
        self.assertEqual("frn", self.ukw_transmitter.rds_id)

    def test_location(self):
        print(self.ukw_transmitter.location[1])
        self.assertListEqual(
            [-33.8688197, 151.2092955],
            list(float(c) for c in self.ukw_transmitter.location))

    def test_transmission_power(self):
        self.assertEqual(1500, self.ukw_transmitter.transmission_power)

    def test_transmission_range(self):
        self.assertEqual(50, self.ukw_transmitter.transmission_range)

    def test_from(self):
        self.assertEqual(
            datetime.time(10, 0, 0), self.ukw_transmitter.transmission_from)

    def test_to(self):
        self.assertEqual(
            datetime.time(20, 0, 0), self.ukw_transmitter.transmission_to)

    def test_station(self):
        self.assertEqual(self.station, self.ukw_transmitter.station)

    def test_instance_to_str(self):
        self.assertEqual('Petersberg - 95.9 MHz', str(self.ukw_transmitter))


class StreamTransmitterModelTest(TestCase):

    def setUp(self):
        self.station = Station.objects.create()
        self.stream_transmitter = StreamTransmitter.objects.create(
            station=self.station,
            url="http://stream.example.com/nice",
            content_type=1,
            bitrate=160,
            transmission_from=datetime.time(10, 0, 0),
            transmission_to=datetime.time(20, 0, 0))

    def test_content_types(self):
        self.assertEqual(
            StreamTransmitter.CONTENT_TYPE,
            (
                (1, 'audio/mpeg'),
                (2, 'application/ogg'),
            ))

    def test_url(self):
        self.assertEqual(
            "http://stream.example.com/nice", self.stream_transmitter.url)

    def test_content_type(self):
        self.assertEqual(1, self.stream_transmitter.content_type)

    def test_bitrate(self):
        self.assertEqual(160, self.stream_transmitter.bitrate)

    def test_from(self):
        self.assertEqual(
            datetime.time(10, 0, 0), self.stream_transmitter.transmission_from)

    def test_to(self):
        self.assertEqual(
            datetime.time(20, 0, 0), self.stream_transmitter.transmission_to)

    def test_station(self):
        self.assertEqual(self.station, self.stream_transmitter.station)
