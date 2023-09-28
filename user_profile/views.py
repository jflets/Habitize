from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from cloudinary import uploader
from .models import UserProfile
from .forms import UserProfileForm

@login_required(login_url="/accounts/login")
def view_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    context = {'user_profile': user_profile}
    return render(request, 'user_profile/view_profile.html', context)

class EditProfileView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'user_profile/edit_profile.html'
    success_url = reverse_lazy('view_profile')

    def get_object(self, queryset=None):
        return UserProfile.objects.get(user=self.request.user)

    def form_valid(self, form):
    # Check if any changes were made to the form data
        if form.has_changed():
            new_username = form.cleaned_data.get('username')

            if new_username and self.request.user.username != new_username:
                self.request.user.username = new_username
                self.request.user.save()

            profile_image = form.cleaned_data['profile_image']

            if profile_image:
                try:
                    # Upload the profile image to Cloudinary
                    response = uploader.upload(profile_image)

                    # Get the public_id from the Cloudinary response
                    public_id = response['public_id']

                    # Save the public_id to the user's profile
                    self.request.user.userprofile.profile_image_public_id = public_id
                except Exception as e:
                    # Handle any exceptions during the upload (e.g., network issues, Cloudinary errors)
                    # You should customize this error handling based on your application's requirements
                    print(f"Error uploading profile image: {str(e)}")
            else:
                # No new profile image provided, retain the existing public_id
                public_id = self.request.user.userprofile.profile_image_public_id

            # Update the user's selected color theme
            new_color_theme = form.cleaned_data['color_theme']
            old_color_theme = self.request.user.userprofile.color_theme

            if new_color_theme != old_color_theme:
                # Only update the session and re-render if the theme has changed
                self.request.user.userprofile.color_theme = new_color_theme
                self.request.user.userprofile.save()

                # Apply the selected color theme to the user's session
                self.request.session['selected_color_theme'] = new_color_theme

        return super().form_valid(form)

