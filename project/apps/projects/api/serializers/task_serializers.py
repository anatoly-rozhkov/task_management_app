from rest_framework import serializers

from apps.projects.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "name", "created_at", "project")
        read_only_fields = ("id",)


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "name", "created_at", "project")
        read_only_fields = ("id", "name", "created_at", "project")
