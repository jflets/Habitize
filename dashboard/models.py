from django.db import models
from django.contrib.auth.models import User


class Habit(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    completed = models.BooleanField(null=False, blank=False, default=False)

    user = models.ForeignKey(
        User, max_length=10, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['completed']
