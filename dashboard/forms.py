from django import forms
from django.core.exceptions import ValidationError
from .models import Habit, Category

class GoalAmountValidationMixin(forms.ModelForm):
    def clean_goal_amount(self):
        goal_amount = self.cleaned_data.get('goal_amount')

        if goal_amount is not None and len(str(goal_amount)) > 4:
            raise ValidationError("Goal amount cannot be more than 4 digits.")

        return goal_amount

class AddHabitForm(GoalAmountValidationMixin, forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'goal_amount', 'units', 'frequency', 'completed', 'category']
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

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=True,
        empty_label="Select a category"
    )

class EditHabitForm(GoalAmountValidationMixin, forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'units', 'value', 'frequency', 'goal_amount', 'completed', 'category']
        labels = {
            'name': 'Habit Name',
            'value': 'Current Amount',
            'goal_amount': 'Goal',
            'completed': 'Completed',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter the habit name'}),
            'units': forms.TextInput(attrs={'placeholder': 'Enter custom units'}),
            'completed': forms.CheckboxInput(),
        }

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=True,
        empty_label='Select a category'
    )
