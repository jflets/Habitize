from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import UserProfile, COLOR_CHOICES
from .forms import UserProfileForm

class UserProfileModelTestCase(TestCase):
    def setUp(self):
        # Create a user and a user profile for testing
        self.user = User.objects.create(username='testuser')
        self.user_profile = UserProfile.objects.create(user=self.user)

    def test_user_profile_creation(self):
        # Test if the user profile is created correctly
        user_profile = UserProfile.objects.get(id=self.user_profile.id)
        self.assertEqual(user_profile.user, self.user)
        self.assertEqual(user_profile.color_theme, 'default')
        self.assertEqual(user_profile.selected_color_theme, 'default')
        self.assertIsNone(user_profile.profile_image)
        self.assertEqual(user_profile.profile_image_public_id, '')

class UserProfileViewTestCase(TestCase):
    def setUp(self):
        # Create a user, set their password, and log them in for testing
        self.user = User.objects.create(username='testuser')
        self.user.set_password('password')
        self.user.save()
        self.client.login(username='testuser', password='password')
        self.user_profile = UserProfile.objects.create(user=self.user)

    def test_view_profile(self):
        # Test the view_profile view to ensure it returns a 200 status code
        url = reverse('view_profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_edit_profile(self):
        # Test the edit_profile view to ensure it returns a 200 status code
        url = reverse('edit_profile', kwargs={'pk': self.user_profile.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class UserProfileFormTestCase(TestCase):
    def test_user_profile_form_valid(self):
        # Test if the UserProfileForm is valid with valid data
        form_data = {
            'color_theme': 'blue',
        }
        form = UserProfileForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_profile_form_invalid(self):
        # Test if the UserProfileForm is invalid with invalid data
        form_data = {
            'color_theme': 'invalid_theme',
        }
        form = UserProfileForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_profile_form_username_valid(self):
        # Test if the UserProfileForm is valid with a valid username
        form_data = {
            'color_theme': 'blue',
            'username': 'newusername',
        }
        form = UserProfileForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_profile_form_username_invalid(self):
        # Test if the UserProfileForm is invalid with an existing username
        # that already exists in the database
        User.objects.create(username='newusername')
        form_data = {
            'color_theme': 'blue',
            'username': 'newusername',
        }
        form = UserProfileForm(data=form_data)
        self.assertFalse(form.is_valid())
