from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount
import cloudinary


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=False)
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ('color_theme', 'profile_image')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.is_google_user = False  # Default to False

    def clean(self):
        cleaned_data = super().clean()
        user = self.instance.user

        # Check if the user signed in with Google
        self.is_google_user = SocialAccount.objects.filter(
            user=user, provider='google').exists()

        # If signed in with Google, disable the username field
        if self.is_google_user:
            self.fields['username'].widget.attrs['readonly'] = True
            self.fields['username'].required = False
            # Make the field not required
            self.fields['username'].help_text =\
                "You signed in with Google. Username cannot be changed."

        return cleaned_data

    def clean_username(self):
        # Get the cleaned username (could be empty)
        username = self.cleaned_data.get('username', None)

        # Check if the username is not None and
        # is not the same as the current username
        if username and User.objects.exclude(pk=self.instance.
                                             user_id).filter(
                                                 username=username).exists():
            raise forms.ValidationError("This username is already in use."
                                        "Please choose a different one.")

        return username

    def clean_profile_image(self):
        profile_image = self.cleaned_data.get('profile_image')

        if profile_image:
            # Fetch information about the image from Cloudinary
            response = cloudinary.api.resource(profile_image.public_id)

            # Check if the image size is greater than 5 MB
            max_size = 5 * 1024 * 1024  # 5 MB in bytes
            if 'bytes' in response and response['bytes'] > max_size:
                raise forms.ValidationError("File size must be"
                                            "no more than 5 MB.")

        return profile_image
