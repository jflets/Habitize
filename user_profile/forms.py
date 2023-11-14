from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount
import cloudinary
from cloudinary import uploader


class UserProfileForm(forms.ModelForm):
    """
    Form for updating user profile information.

    Includes fields for changing the username, color theme, and profile image.
    """
    username = forms.CharField(max_length=15, required=True)
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ('color_theme', 'profile_image')

    def __init__(self, *args, **kwargs):
        """
        Initialize the UserProfileForm.
        """
        super(UserProfileForm, self).__init__(*args, **kwargs)

    def clean_username(self):
        """
        Validate the uniqueness of the username.

        Checks if the provided username is already in use.
        """
        username = self.cleaned_data.get('username', None)

        if username and User.objects.exclude(
                                pk=self.instance.user_id).filter(
                                    username=username).exists():
            raise forms.ValidationError("This username is already in use."
                                        "Please choose a different one.")

        return username

    def clean_profile_image(self):
        """
        Validate and handle the profile image.

        Checks the size of the image and uploads it to Cloudinary if needed.
        """
        profile_image = self.cleaned_data.get('profile_image')

        if not profile_image:
            return self.instance.profile_image

        if isinstance(profile_image, cloudinary.models.CloudinaryField):
            return profile_image.public_id

        if isinstance(profile_image, cloudinary.models.CloudinaryResource):
            return profile_image.public_id

        if profile_image.size > 5 * 1024 * 1024:  # 5MB in bytes
            raise forms.ValidationError("Image size must be 5MB or less.")

        try:
            response = uploader.upload(profile_image)

            if 'public_id' in response:
                public_id = response['public_id']
                return public_id
            else:
                raise forms.ValidationError("Failed to"
                                            "upload image to Cloudinary")
        except cloudinary.api.Error as e:
            raise forms.ValidationError(f"Cloudinary API error: {str(e)}")
        except Exception as e:
            raise forms.ValidationError(f"Error uploading image: {str(e)}")
