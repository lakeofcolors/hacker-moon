from django.test import TestCase

# Create your tests here.

class HomePageTest(TestCase):

    def test_homepage_status(self):

        response = self.client.get('/')

        self.assertEqual(response.status_code,200)
