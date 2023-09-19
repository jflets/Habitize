from . import views
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', views.get_dashboard, name='dashboard'),
]
