from django.contrib import admin
from .models import Habit, Category


class HabitAdmin(admin.ModelAdmin):
    """Custom admin configuration for the Habit model."""

    list_display = ('name', 'get_user_username', 'frequency',
                    'completed', 'value', 'goal_amount')

    def get_user_username(self, obj):
        """Get the username of the associated user or an empty string
          if not available."""
        return obj.user.username if obj.user else ''

    get_user_username.short_description = 'User'


admin.site.register(Habit, HabitAdmin)
admin.site.register(Category)
