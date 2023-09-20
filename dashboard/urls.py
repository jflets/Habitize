from . import views
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', views.get_dashboard, name='dashboard'),
    path('add', views.add_habit, name='add'),
    path('edit/<habit_id>', views.edit_habit, name='edit'),
]
