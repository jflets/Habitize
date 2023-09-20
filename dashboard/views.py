from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Habit
from .forms import HabitForm


@login_required(login_url="/accounts/login")
def get_dashboard(request):
    habits = Habit.objects.filter(user=request.user)

    # Calculate progress for each habit
    for habit in habits:
        habit.progress = (habit.value / habit.max_value) * \
            100 if habit.max_value > 0 else 0

    context = {
        'habits': habits,
    }
    return render(request, 'dashboard/index.html', context)


@login_required(login_url="/accounts/login")
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('dashboard')
    else:
        form = HabitForm()

    context = {
        'form': form
    }
    return render(request, 'dashboard/add_habit.html', context)


@login_required(login_url="/accounts/login")
def edit_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)

    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            habit = form.save()
            return redirect('dashboard')
    else:
        form = HabitForm(instance=habit)

    context = {
        'form': form,
        'progress_percentage': (habit.value / habit.max_value) * 100,
    }
    return render(request, 'dashboard/edit_habit.html', context)


@login_required(login_url="/accounts/login")
def toggle_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)
    habit.completed = not habit.completed
    habit.save()
    return redirect('dashboard')


@login_required(login_url="/accounts/login")
def delete_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)
    habit.delete()
    return redirect('dashboard')
