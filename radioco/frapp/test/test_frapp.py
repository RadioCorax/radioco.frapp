import datetime
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.test import TestCase
from radioco.frapp.models import Station, Studio


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


class StudioModelTest(TestCase):

    def setUp(self):
        self.station = Station.objects.create()
        self.studio = Studio.objects.create(
            station=self.station,
            city="Halle (Saale)",
            street="Somestreet",
            number=123,
            zip=99999,
            open_from=datetime.time(10, 0, 0),
            open_to=datetime.time(20, 0, 0))

    def test_street(self):
        self.assertEqual("Somestreet", self.studio.street)

    def test_number(self):
        self.assertEqual(123, self.studio.number)

    def test_city(self):
        self.assertEqual("Halle (Saale)", self.studio.city)

    def test_zip(self):
        self.assertEqual(99999, self.studio.zip)

    def test_open_from(self):
        self.assertEqual(datetime.time(10, 0, 0), self.studio.open_from)

    def test_open_to(self):
        self.assertEqual(datetime.time(20, 0, 0), self.studio.open_to)

    def test_station(self):
        self.assertEqual(self.station, self.studio.station)


class StationViewTest(TestCase):
    def test_valid_response(self):
        response = self.client.get(reverse('frapp:index'))
        self.assertEqual(response.status_code, 200)

    def test_content_type(self):
        response = self.client.get(reverse('frapp:index'))
        self.assertEqual(response.status_code, 200)
