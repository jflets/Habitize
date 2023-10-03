from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Habit

class DashboardTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

    def test_dashboard_view(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Access the dashboard view
        url = reverse('dashboard')
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_add_habit_view(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Access the add habit view
        url = reverse('add')
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)