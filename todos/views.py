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


def view_task(request, id):
    task = Task.objects.get(id=id)
    context = {"task": task}
    return render(request, "todos/view_task.html", context)


def add_task(request):
    form = AddTaskForm()
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "todos/add_task.html", context)


def update_task(request, id):
    task = Task.objects.get(id=id)
    form = AddTaskForm(instance=task)
    if request.method == "POST":
        form = AddTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "todos/update_task.html", context)


def delete_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        task.delete()
        return redirect("home")
    context = {"task": task}
    return render(request, "todos/delete_task.html", context)
