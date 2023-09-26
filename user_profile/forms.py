from django import forms
from .models import UserProfile
from django.contrib.auth.models import User  # Import User model


class UserProfileForm(forms.ModelForm):
    # Add a new field for the username
    username = forms.CharField(max_length=150, required=True)

    class Meta:
        model = UserProfile
        # Include 'color_theme' and 'profile_image' as before
        fields = ('color_theme', 'profile_image')

    def clean_username(self):
        # Validate and ensure the username is unique
        username = self.cleaned_data.get('username')
        if User.objects.exclude(pk=self.instance.user_id).filter(username=username).exists():
            raise forms.ValidationError(
                "This username is already in use. Please choose a different one.")
        return username
