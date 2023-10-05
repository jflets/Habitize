from . import views
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landingPage, name='home'),
    path('help', views.HelpPage, name='help'),
    path('thank-you', views.thankYouPage, name='thank-you'),
]
