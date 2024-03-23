from django.urls import path
from . import views

urlpatterns = [
    path("tasks/", views.list_tasks, name="api-tasks"),
    path("task/<uuid:id>/", views.task_detail, name="api-task-detail"),
]
