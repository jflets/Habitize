from django import forms
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from cloudinary import uploader
from .models import UserProfile, COLOR_CHOICES
from .forms import UserProfileForm


@login_required(login_url="/accounts/login")
def view_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.
                                                              user)

    if not user_profile.profile_image_public_id:
        user_profile.profile_image_public_id = \
            '/static/images/profile-image-icon.webp'
        user_profile.save()

    context = {'user_profile': user_profile}
    return render(request, 'user_profile/view_profile.html', context)


class EditProfileView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'user_profile/edit_profile.html'
    success_url = reverse_lazy('view_profile')

    def get_initial(self):
        initial = super().get_initial()
        # Set the initial username to the current user's username
        initial['username'] = self.request.user.username
        return initial

    def form_valid(self, form):
        # Check if any changes were made to the form data
        if form.has_changed():
            new_username = form.cleaned_data.get('username')

            if new_username and self.request.user.username != new_username:
                # Check if the new username is already in use
                if User.objects.exclude(pk=self.request.
                                        user.pk).filter(username=new_username
                                                        ).exists():
                    raise ValidationError("This username"
                                          "is already in use."
                                          "Please choose a different one.")
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
                    self.request.user.userprofile.profile_image_public_id =\
                        public_id
                except Exception as e:
                    # Handle any exceptions during the upload
                    # (e.g., network issues, Cloudinary errors)
                    print(f"Error uploading profile image: {str(e)}")
            else:
                # No new profile image provided, retain the existing public_id
                public_id =\
                    self.request.user.userprofile.profile_image_public_id

            new_color_theme = form.cleaned_data['color_theme']
            old_color_theme = self.request.user.userprofile.color_theme

            if new_color_theme != old_color_theme:
                self.request.user.userprofile.color_theme = new_color_theme
                self.request.user.userprofile.save()

                # Apply the selected color theme to the user's session
                self.request.session['selected_color_theme'] = new_color_theme

            messages.success(self.request, 'Profile updated successfully!')

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['color_choices'] = COLOR_CHOICES
        return context

    @receiver(user_logged_in)
    def set_color_theme_session(sender, request, user, **kwargs):
        if hasattr(user, 'userprofile') and user.userprofile.color_theme:
            request.session['selected_color'
                            '_theme'] = user.userprofile.color_theme
