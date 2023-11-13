from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount
import cloudinary
from cloudinary import uploader, api


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=15, required=False)
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

        # If no new image is provided, return the existing public_id (if any)
        if not profile_image:
            return self.instance.profile_image

        # Check if it's a CloudinaryField instance
        if isinstance(profile_image, cloudinary.models.CloudinaryField):
            return profile_image.public_id

        # Check if the image is a CloudinaryResource
        if isinstance(profile_image, cloudinary.models.CloudinaryResource):
            # Return the public_id from the CloudinaryResource
            return profile_image.public_id

        # Check if the image size is greater than 5MB
        if profile_image.size > 5 * 1024 * 1024:  # 5MB in bytes
            raise forms.ValidationError("Image size must be 5MB or less.")

        try:
            # Upload the file to Cloudinary
            response = uploader.upload(profile_image)

            # Check if the upload was successful
            if 'public_id' in response:
                # Access the public_id attribute
                public_id = response['public_id']
                # You can store or use the public_id as needed
                return public_id
            else:
                raise forms.ValidationError("Failed to upload"
                                            "image to Cloudinary")
        except cloudinary.api.Error as e:
            raise forms.ValidationError(f"Cloudinary API error: {str(e)}")
        except Exception as e:
            raise forms.ValidationError(f"Error uploading image: {str(e)}")
