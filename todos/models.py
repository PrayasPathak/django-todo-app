from django.db import models
import uuid


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    due_date = models.DateField()
    due_time = models.TimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} | {self.id} | {self.due_date}"
