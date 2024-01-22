from django.shortcuts import render, redirect


# App level imports
from .models import Task
from .forms import AddTaskForm


def index(request):
    tasks = Task.objects.all()
    context = {
        "tasks": tasks,
    }
    return render(request, "todos/index.html", context)


def add_task(request):
    form = AddTaskForm()
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "todos/add_task.html", context)
