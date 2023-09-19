from . import views
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landingPage, name='home'),
]
