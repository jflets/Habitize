from django.contrib import admin
from .models import Habit, Category


class HabitAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_user_username', 'frequency',
                    'completed', 'value', 'goal_amount')

    def get_user_username(self, obj):
        return obj.user.username if obj.user else ''

    get_user_username.short_description = 'User'


admin.site.register(Habit, HabitAdmin)
admin.site.register(Category)
