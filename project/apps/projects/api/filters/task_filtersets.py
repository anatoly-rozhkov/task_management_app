from apps.projects.models import Task, Project
from django_filters.rest_framework import FilterSet, ModelChoiceFilter


class TaskFilter(FilterSet):
    project = ModelChoiceFilter(queryset=Project.objects.all())

    class Meta:
        model = Task
        fields = ["project"]
