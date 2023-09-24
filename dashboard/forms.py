from django import forms
from .models import Habit


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'completed', 'value', 'goal_amount']
        labels = {
            'name': 'Habit Name',
            'completed': 'Completed',
            'value': 'Value',
            'goal_amount': 'Goal Amount',
        }
        widgets = {
            'value': forms.NumberInput(attrs={'type': 'number', 'placeholder': 'Enter a value'}),
        }
