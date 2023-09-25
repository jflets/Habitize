from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Habit
from .forms import AddHabitForm, EditHabitForm


@login_required(login_url="/accounts/login")
def get_dashboard(request):
    habits = Habit.objects.filter(user=request.user)
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

    context = {
        'habits': habits,
        'total_habits': total_habits,
        'completed_habits': completed_habits,
        'total_completed_progress': total_completed_progress,
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
            habit = form.save()
            return redirect('dashboard')
    else:
        form = EditHabitForm(instance=habit)

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

    # Set the value equal to the goal_amount when completed
    habit.value = habit.goal_amount

    habit.save()

    return redirect('dashboard')


@login_required(login_url="/accounts/login")
def delete_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)

    if request.method == 'POST':
        # Check if the user confirmed the deletion
        if 'confirm_delete' in request.POST:
            habit.delete()
            return redirect('dashboard')
        else:
            # If not confirmed, redirect back to the habit list
            return redirect('dashboard')

    context = {'habit': habit}
    return render(request, 'dashboard/delete_confirmation.html', context)
