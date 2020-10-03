from django.urls import reverse
from django.test import TestCase


class StationViewTest(TestCase):
    def test_valid_response(self):
        response = self.client.get(reverse('frapp:index'))
        self.assertEqual(response.status_code, 200)

    def test_content_type(self):
        response = self.client.get(reverse('frapp:index'))
        self.assertEqual(response.status_code, 200)
