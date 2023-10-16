"""habitize URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
