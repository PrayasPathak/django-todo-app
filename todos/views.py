from django.shortcuts import render, redirect


# App level imports
# from .forms import AddTaskForm


def index(request):
    return render(request, "todos/index.html")
