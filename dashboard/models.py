from django.db import models
from django.contrib.auth.models import User


class Habit(models.Model):
    # Existing fields
    name = models.CharField(max_length=50, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    completed = models.BooleanField(null=False, blank=False, default=False)
    value = models.PositiveIntegerField(default=0)  # Current value
    goal_amount = models.PositiveIntegerField(default=100)  # Maximum value

    # New fields
    frequency = models.CharField(
        max_length=10,
        choices=[
            ('day', 'Daily'),
            ('week', 'Weekly'),
            ('month', 'Monthly'),
        ],
        default='day',
        null=False,
        blank=False
    )

    units = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        User, max_length=10, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['completed']
