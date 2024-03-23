from rest_framework import serializers
import uuid

from todos.models import Task


class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=2000)
    id = serializers.UUIDField(default=uuid.uuid4, read_only=True)
    due_date = serializers.DateField()
    due_time = serializers.TimeField()
    completed = serializers.BooleanField(default=False)

    def create(self, validted_data):
        return Task.objects.create(**validted_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.due_date = validated_data.get("due_date", instance.due_date)
        instance.due_time = validated_data.get("due_time", instance.due_time)
        instance.completed = validated_data.get("completed", instance.completed)
        instance.save()
        return instance
