from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField


# color themes
COLOR_CHOICES = [
    ('default', 'Default Theme'),
    ('blue', 'Blue Theme'),
    ('turquoise', 'Turquoise Theme'),
    ('green', 'Green Theme'),
    ('pink', 'Pink Theme'),
    ('purple', 'Purple Theme'),
    ('brown', 'Brown Theme'),
]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    color_theme = models.CharField(
        max_length=20, choices=COLOR_CHOICES, default='default')
    selected_color_theme = models.CharField(max_length=50, default='default')
    profile_image = CloudinaryField('image', null=True, blank=True,
                                    max_length=1024 * 1024 * 5)
    profile_image_public_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
