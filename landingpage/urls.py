from . import views
from django.urls import path

urlpatterns = [
    path('', views.landingPage, name='home'),
]
