from django.db import IntegrityError
from django.test import TestCase
from radioco.frapp.models import Station


class StationModelTest(TestCase):

    def setUp(self):
        self.station_data = Station.objects.create(
            name="RadioCo Test Station",
            display_name="RadioCo",
            city="Halle (Saale)",
            description="Some radio station")

    def test_name(self):
        self.assertEqual("RadioCo Test Station", self.station_data.name)

    def test_display_name(self):
        self.assertEqual("RadioCo", self.station_data.display_name)

    def test_city(self):
        self.assertEqual("Halle (Saale)", self.station_data.city)

    def test_description(self):
        self.assertEqual("Some radio station", self.station_data.description)

    def test_singleton(self):
        with self.assertRaises(IntegrityError):
            Station.objects.create()
