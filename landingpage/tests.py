from django.test import TestCase
from django.urls import reverse

class LandingPageViewTestCase(TestCase):
    def test_view_url_exists_at_desired_location(self):
        # Check if the URL for the landingPage view exists and returns a 200 status code.
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        # Check if the landingPage view can be accessed by its name.
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        # Check if the landingPage view uses the correct template.
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'landing_page/index.html')
