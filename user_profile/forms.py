from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    # Add a new field for the username
    username = forms.CharField(max_length=150, required=False)
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        # Include 'color_theme' and 'profile_image' as before
        fields = ('color_theme', 'profile_image')

    def clean_username(self):
        # Get the cleaned username (could be empty)
        username = self.cleaned_data.get('username', None)

        # Check if the username is not None and is
        # not the same as the current username
        if username and User.objects.exclude(pk=self.instance.user_id
                                             ).filter(username=username
                                                      ).exists():
            raise forms.ValidationError(
                "This username is already in use."
                " Please choose a different one.")

        return username
