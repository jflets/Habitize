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
    """
    View function for displaying the user profile.

    Retrieves the user profile and ensures that a default profile image is set.
    Renders the 'view_profile.html' template with the user profile context.
    """
    user_profile, created = UserProfile.objects.get_or_create(
        user=request.user)

    if not user_profile.profile_image_public_id:
        user_profile.profile_image_public_id = \
            '/static/images/profile-image-icon.webp'
        user_profile.save()

    context = {'user_profile': user_profile}
    return render(request, 'user_profile/view_profile.html', context)


class EditProfileView(UpdateView):
    """
    Class-based view for editing the user profile.

    Uses the UserProfile model and UserProfileForm for editing user
    information.
    Redirects to 'view_profile' upon successful form submission.

    Methods:
    - get_initial: Sets the initial username to the current user's username.
    - form_valid: Handles form submission, validates changes,
    and updates the user's profile.
    - get_context_data: Adds color choices to the context.
    """
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'user_profile/edit_profile.html'
    success_url = reverse_lazy('view_profile')

    def get_initial(self):
        """
        Set the initial username to the current user's username.
        """
        initial = super().get_initial()
        initial['username'] = self.request.user.username
        return initial

    def form_valid(self, form):
        """
        Handle form submission, validate changes, and update the user's
        profile.

        Checks for changes in the form data and updates the user's username,
        profile image, color theme, and session accordingly.

        Raises a ValidationError if the new username is already in use.

        Displays a success message upon successful profile update.
        """
        if form.has_changed():
            new_username = form.cleaned_data.get('username')

            if new_username and self.request.user.username != new_username:
                if User.objects.exclude(
                    pk=self.request.user.pk).filter(
                        username=new_username).exists():
                    raise ValidationError("This username is already in use."
                                          "Please choose a different one.")
                self.request.user.username = new_username
                self.request.user.save()

            profile_image = form.cleaned_data['profile_image']

            if profile_image:
                try:
                    response = uploader.upload(profile_image)
                    public_id = response['public_id']
                    self.request.user.userprofile.profile_image_public_id =\
                        public_id
                except Exception as e:
                    print(f"Error uploading profile image: {str(e)}")
            else:
                public_id =\
                    self.request.user.userprofile.profile_image_public_id

            new_color_theme = form.cleaned_data['color_theme']
            old_color_theme = self.request.user.userprofile.color_theme

            if new_color_theme != old_color_theme:
                self.request.user.userprofile.color_theme = new_color_theme
                self.request.user.userprofile.save()
                self.request.session['selected_color_theme'] = new_color_theme

            messages.success(self.request, 'Profile updated successfully!')

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Add color choices to the context.
        """
        context = super().get_context_data(**kwargs)
        context['color_choices'] = COLOR_CHOICES
        return context

    @receiver(user_logged_in)
    def set_color_theme_session(sender, request, user, **kwargs):
        """
        Signal receiver to set the color theme in the session upon user login.
        """
        if hasattr(user, 'userprofile') and user.userprofile.color_theme:
            request.session['selected_color_theme'] =\
                user.userprofile.color_theme
