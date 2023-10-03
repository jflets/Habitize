from . import views
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', views.view_profile, name='view_profile'),
    path('edit/<int:pk>/', views.EditProfileView.as_view(), name='edit_profile'),
]
