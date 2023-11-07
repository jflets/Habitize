from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Habit
from .forms import AddHabitForm, EditHabitForm
from user_profile.models import UserProfile


@login_required(login_url="/accounts/login")
def get_dashboard(request):
    # Get the selected frequency from the request
    selected_frequency = request.GET.get('frequency')

    # Filter habits based on the selected frequency
    habits = Habit.objects.filter(user=request.user)

    if selected_frequency == 'day':
        habits = habits.filter(frequency='day')
    elif selected_frequency == 'week':
        habits = habits.filter(frequency='week')
    elif selected_frequency == 'month':
        habits = habits.filter(frequency='month')
    else:
        # Handle cases where an invalid frequency is selected
        habits = habits.all()
        # Display all habits, you can customize this behavior

    total_habits = habits.count()
    completed_habits = habits.filter(completed=True).count()

    # Calculate progress for each habit
    for habit in habits:
        if habit.completed:
            # If the habit is completed, set progress to 100%
            habit.progress = 100
        else:
            # Calculate progress based on value and goal_amount
            habit.progress = (habit.value / habit.goal_amount) * \
                100 if habit.goal_amount > 0 else 0

    # Calculate progress for total completed habits
    total_completed_progress = (
        completed_habits / total_habits) * 100 if total_habits > 0 else 0

    # Calculate progress for completed habits by frequency
    completed_habits_day = habits.filter(
        completed=True, frequency='day').count()
    completed_habits_week = habits.filter(
        completed=True, frequency='week').count()
    completed_habits_month = habits.filter(
        completed=True, frequency='month').count()

    # Calculate the ratio of completed habits for each frequency
    total_habits_day = habits.filter(frequency='day').count()
    total_habits_week = habits.filter(frequency='week').count()
    total_habits_month = habits.filter(frequency='month').count()

    completed_progress_day = (
        completed_habits_day /
        total_habits_day) * 100 if total_habits_day > 0 else 0
    completed_progress_week = (
        completed_habits_week /
        total_habits_week) * 100 if total_habits_week > 0 else 0
    completed_progress_month = (
        completed_habits_month /
        total_habits_month * 100) if total_habits_month > 0 else 0

    context = {
        'habits': habits,
        'total_habits': total_habits,
        'completed_habits': completed_habits,
        'total_completed_progress': total_completed_progress,
        'selected_frequency': selected_frequency,
        'completed_habits_day': completed_habits_day,
        'completed_habits_week': completed_habits_week,
        'completed_habits_month': completed_habits_month,
        'completed_progress_day': completed_progress_day,
        'completed_progress_week': completed_progress_week,
        'completed_progress_month': completed_progress_month,
        'total_habits_day': total_habits_day,
        'total_habits_week': total_habits_week,
        'total_habits_month': total_habits_month,
    }
    return render(request, 'dashboard/index.html', context)


@login_required(login_url="/accounts/login")
def add_habit(request):
    if request.method == 'POST':
        form = AddHabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            messages.success(request, 'Habit added successfully.')
            return redirect('dashboard')
    else:
        form = AddHabitForm()

    context = {
        'form': form
    }
    return render(request, 'dashboard/add_habit.html', context)


@login_required(login_url="/accounts/login")
def edit_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)

    if request.method == 'POST':
        form = EditHabitForm(request.POST, instance=habit)
        if form.is_valid():
            # Check if "completed" checkbox is checked
            completed = form.cleaned_data['completed']
            # Check if the "current amount" matches the "goal amount"
            current_amount = form.cleaned_data['value']
            goal_amount = form.cleaned_data['goal_amount']

            if current_amount == goal_amount:
                # If the "current amount" matches the "goal amount," mark the habit as complete
                habit.completed = True
            elif completed:
                # If the "completed" checkbox is checked, set the "current amount" to the "goal amount"
                habit.value = goal_amount

            # Manually set the "value" field to its current value to preserve the read-only state
            form.instance.value = habit.value
            form.save()
            messages.success(request, 'Habit edited successfully.')
            return redirect('dashboard')
    else:
        form = EditHabitForm(instance=habit)

    # Make the "value" input field readonly in the template
    form.fields['value'].widget.attrs['readonly'] = 'readonly'

    context = {
        'form': form,
        'progress_percentage': (habit.value / habit.goal_amount) * 100,
    }
    return render(request, 'dashboard/edit_habit.html', context)


@login_required(login_url="/accounts/login")
def toggle_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)

    if habit.completed:
        # If the habit is already completed, redirect back to the dashboard
        return redirect('dashboard')

    # If the habit is not completed, mark it as completed
    habit.completed = True
    habit.progress = 100
    habit.value = habit.goal_amount

    # Set the completion date to the current date and time
    habit.date_completed = timezone.now().date()

    habit.save()
    messages.success(request, 'Habit Completed.')

    return redirect('dashboard')


@login_required(login_url="/accounts/login")
def delete_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)

    if request.method == 'POST':
        # Check if the user confirmed the deletion
        if 'confirm_delete' in request.POST:
            habit.delete()
            messages.success(request, 'Habit deleted successfully.')
            return redirect('dashboard')
        else:
            # If not confirmed, redirect back to the habit list
            return redirect('dashboard')

    context = {'habit': habit}
    return render(request, 'dashboard/delete_confirmation.html', context)


@login_required(login_url="/accounts/login")
def set_selected_color_theme(request, color_theme):
    # Check if the selected color theme is valid
    valid_color_themes = ['default', 'blue', 'turquoise',
                          'green', 'pink', 'purple', 'brown']

    if color_theme not in valid_color_themes:
        messages.error(request, 'Invalid color theme selected.')
        return redirect('dashboard')

    # Get the user's UserProfile instance
    user_profile, created = UserProfile.objects.get_or_create(user=request.
                                                              user)

    # Set the selected color theme in the user's profile
    user_profile.selected_color_theme = color_theme
    user_profile.save()

    # Set the selected color theme in the session
    request.session['selected_color_theme'] = color_theme

    messages.success(request,
                     f'Color theme set to{color_theme.capitalize()}.')

    return redirect('dashboard')
