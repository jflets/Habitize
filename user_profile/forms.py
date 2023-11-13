from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=False)
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ('color_theme', 'profile_image')

    def clean_username(self):
        username = self.cleaned_data.get('username', None)

        if username and User.objects.exclude(pk=self.instance.user_id).filter(username=username).exists():
            raise forms.ValidationError("This username is already in use. Please choose a different one.")

        return username

    def clean_profile_image(self):
        profile_image = self.cleaned_data.get('profile_image')

        # Check if the uploaded image size exceeds the allowed limit (5 MB)
        max_size = 5 * 1024 * 1024  # 5 MB in bytes
        if profile_image and profile_image.size > max_size:
            raise forms.ValidationError("File size must be no more than 5 MB.")

        return profile_image
