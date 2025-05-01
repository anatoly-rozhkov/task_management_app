from rest_framework import serializers

from apps.projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "name", "created_at", "description", "due_date", "user")
        read_only_fields = (
            "id",
            "user",
            "created_at",
        )


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "name", "created_at", "description", "due_date", "user")
        read_only_fields = ("id", "name", "created_at", "description", "due_date", "user")
