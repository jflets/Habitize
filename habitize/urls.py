from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.conf.urls import handler403
from .views import custom_404_view, custom_500_view, custom_403_view

handler404 = 'habitize.views.custom_404_view'
handler403 = 'habitize.views.custom_403_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landingpage.urls'), name='landingpage_urls'),
    path("accounts/", include("allauth.urls")),
    path('dashboard/', include('dashboard.urls'), name='dashboard_urls'),
    path('profile/', include('user_profile.urls'), name='user_profile'),
    path('500/', custom_500_view, name='custom_500'),
]
