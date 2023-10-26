from django import forms
from django.forms import TimeInput
from .models import Habit, Category


class AddHabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'goal_amount', 'units',
                  'frequency', 'completed', 'category']
        labels = {
            'name': 'Habit Name',
            'completed': 'Completed',
            'goal_amount': 'Goal',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':
                                           'Enter the habit name'}),
            'units': forms.TextInput(attrs={'placeholder':
                                            'Enter custom units'}),
            'value': forms.NumberInput(attrs={'type': 'number', 'placeholder':
                                              'Enter a value'}),
        }

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=True,
        empty_label="Select a category"
    )

class EditHabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'units', 'value', 'frequency',
                  'goal_amount', 'completed', 'category']
        labels = {
            'name': 'Habit Name',
            'value': 'Current Amount',
            'goal_amount': 'Goal',
            'completed': 'Completed',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':
                                           'Enter the habit name'}),
            'units': forms.TextInput(attrs={'placeholder':
                                            'Enter custom units'}),
            'value': forms.NumberInput(attrs={'type': 'number', 'placeholder':
                                              'Enter a value', 'readonly':
                                              'readonly'}),
        }

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=True,
        empty_label='Other'
    )
