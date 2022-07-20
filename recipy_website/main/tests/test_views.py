from django.test import TestCase
from django.urls import reverse

class HomeViewTest(TestCase):
    template_location = 'main/home.html'
    url = reverse('home')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)