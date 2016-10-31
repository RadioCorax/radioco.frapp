import datetime
from django.test import TestCase
from radioco.frapp.models import Station, Studio


class StudioModelTest(TestCase):

    def setUp(self):
        self.station = Station.objects.create()
        self.studio = Studio.objects.create(
            station=self.station,
            city="Halle (Saale)",
            street="Somestreet",
            number=123,
            zip=99999,
            email="me@example.com",
            phone="+49 234 123123123",
            location_latitude=-33.8688197,
            location_longitude=151.20929550000005,
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

    def test_email(self):
        self.assertEqual("me@example.com", self.studio.email)

    def test_phone(self):
        self.assertEqual("+49 234 123123123", self.studio.phone)

    def test_location(self):
        self.assertEqual(
            "-33.8688197 151.2092955", self.studio.location)

    def test_open_from(self):
        self.assertEqual(datetime.time(10, 0, 0), self.studio.open_from)

    def test_open_to(self):
        self.assertEqual(datetime.time(20, 0, 0), self.studio.open_to)

    def test_station(self):
        self.assertEqual(self.station, self.studio.station)

    def test_unicode(self):
        self.assertEqual(
            u'Halle (Saale) - Somestreet 123', unicode(self.studio))
