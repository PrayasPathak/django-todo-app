from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("add/", views.add_task, name="add"),
    path("update/<str:id>/", views.update_task, name="update_task"),
    path("delete/<str:id>/", views.delete_task, name="delete_task"),
    path("view/<str:id>/", views.view_task, name="view_task"),
]
