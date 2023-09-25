from django import forms
from .models import Habit


class AddHabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'goal_amount', 'units', 'frequency', 'completed']
        labels = {
            'name': 'Habit Name',
            'completed': 'Completed',
            'goal_amount': 'Goal',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter the habit name'}),
            'units': forms.TextInput(attrs={'placeholder': 'Enter custom units'}),
            'value': forms.NumberInput(attrs={'type': 'number', 'placeholder': 'Enter a value'}),
        }


class EditHabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'units', 'value',
                  'frequency', 'goal_amount', 'completed']
        labels = {
            'name': 'Habit Name',
            'value': 'Amount',
            'goal_amount': 'Goal',
            'completed': 'Completed',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter the habit name'}),
            'units': forms.TextInput(attrs={'placeholder': 'Enter custom units'}),
            'value': forms.NumberInput(attrs={'type': 'number', 'placeholder': 'Enter a value'}),
        }
