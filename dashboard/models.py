from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.core.validators import MaxValueValidator


class Category(models.Model):
    """Model representing a category for habits."""

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Habit(models.Model):
    """Model representing a habit."""

    name = models.CharField(max_length=11, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    completed = models.BooleanField(null=False, blank=False, default=False)
    value = models.PositiveIntegerField(default=0)
    goal_amount = models.PositiveIntegerField(default=10,
                                              validators=[MaxValueValidator
                                                          (9999)])
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)

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

    last_reset = models.DateTimeField(null=True, blank=True)

    units = models.CharField(
        max_length=6,
        null=True,
        blank=True,
    )

    date_completed = models.DateField(null=True, blank=True)

    user = models.ForeignKey(
        User, max_length=10, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def reset_habit(self):
        """Reset the habit if the reset conditions are met."""
        if self.frequency == 'day':
            reset_period = timedelta(days=1)
        elif self.frequency == 'week':
            reset_period = timedelta(weeks=1)
        elif self.frequency == 'month':
            reset_period = timedelta(days=30)

        # Check if the habit hasn't been reset within the reset_period
        if self.last_reset is None or (timezone.now() -
                                       self.last_reset) >= reset_period:
            # Reset the habit by updating its value and last reset time
            self.value = 0
            self.last_reset = timezone.now()
            self.save()

    def save(self, *args, **kwargs):
        """Save method to update completed status and reset the habit
        before saving."""
        # Check if the current value has reached the goal amount
        if self.value >= self.goal_amount:
            self.completed = True
        else:
            self.completed = False

        # Call the reset_habit method before saving the habit
        self.reset_habit()

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['category', 'completed', 'name']
