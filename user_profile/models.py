from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField


# Define choices for color themes
COLOR_CHOICES = [
    ('light', 'Light Theme'),
    ('dark', 'Dark Theme'),
    # Add more choices as needed
]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    color_theme = models.CharField(
        max_length=20, choices=COLOR_CHOICES, default='light')
    profile_image = CloudinaryField('image', null=True, blank=True)
    profile_image_public_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
