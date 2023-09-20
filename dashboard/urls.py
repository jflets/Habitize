from . import views
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', views.get_dashboard, name='dashboard'),
    path('add', views.add_habit, name='add'),
    path('edit/<habit_id>', views.edit_habit, name='edit'),
    path('toggle/<habit_id>', views.toggle_habit, name='toggle'),
    path('delete/<habit_id>', views.delete_habit, name='delete'),
]
