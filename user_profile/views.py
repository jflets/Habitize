from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from cloudinary.forms import CloudinaryFileField
from .models import UserProfile
from .forms import UserProfileForm


@login_required(login_url="/accounts/login")
def view_profile(request):
    user_profile = UserProfile.objects.get_or_create(user=request.user)[0]
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
        # Handle username change
        new_username = form.cleaned_data['username']
        if self.request.user.username != new_username:
            self.request.user.username = new_username
            self.request.user.save()

        # Handle profile image upload to Cloudinary
        profile_image = form.cleaned_data['profile_image']
        if profile_image:
            # Get the Cloudinary public ID of the uploaded image
            public_id = profile_image.public_id
            self.request.user.userprofile.profile_image_public_id = public_id
            self.request.user.userprofile.save()

        return super().form_valid(form)
