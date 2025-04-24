from drf_spectacular.utils import extend_schema, extend_schema_view

from apps.helpers.extended_viewsets import FullExtendedModelViewSet
from apps.projects.api.filters import TaskFilter

from apps.projects.api.serializers import TaskSerializer, TaskListSerializer
from apps.projects.models import Task


@extend_schema_view(
    list=extend_schema(description="List all tasks."),
    retrieve=extend_schema(description="Get task by id."),
    create=extend_schema(description="Create task."),
    update=extend_schema(description="Update task."),
    partial_update=extend_schema(description="Partially update task."),
    destroy=extend_schema(description="Delete task."),
)
class TaskViewSet(FullExtendedModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_class = TaskFilter
    serializer_class_map = {
        "list": TaskListSerializer,
        "retrieve": TaskListSerializer,
        "create": TaskSerializer,
        "update": TaskSerializer,
        "partial_update": TaskSerializer,
    }
