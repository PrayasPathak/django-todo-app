from django import forms
from django.forms import ModelForm
from .models import Task


class AddTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        exclude = ["id"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Go outing with friends",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Let's go outing outside of city in a week",
                    "rows": 5,
                    "cols": 40,
                }
            ),
            "due_date": forms.NumberInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),
            "due_time": forms.TimeInput(
                attrs={
                    "type": "time",
                    "class": "form-control",
                }
            ),
        }
