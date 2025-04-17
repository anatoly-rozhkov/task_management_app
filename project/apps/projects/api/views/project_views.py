from typing import Any

from rest_framework.request import Request

from rest_framework.decorators import action
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema, extend_schema_view

from apps.helpers.extended_viewsets import FullExtendedModelViewSet

from apps.projects.api.serializers import ProjectSerializer, ProjectListSerializer, TaskListSerializer
from apps.projects.models import Project


@extend_schema_view(
    list=extend_schema(description="List all projects."),
    retrieve=extend_schema(description="Get project by id."),
    create=extend_schema(description="Create project."),
    update=extend_schema(description="Update project."),
    partial_update=extend_schema(description="Partially update project."),
    get_tasks=extend_schema(description="Get tasks by project."),
    destroy=extend_schema(description="Delete project."),
)
class ProjectViewSet(FullExtendedModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    serializer_class_map = {
        "list": ProjectListSerializer,
        "retrieve": ProjectListSerializer,
        "create": ProjectSerializer,
        "update": ProjectSerializer,
        "partial_update": ProjectSerializer,
        "get_tasks": TaskListSerializer,
    }
    # permission_classes = (IsSuperUser,)
    # permission_classes_map = {
    #     "list": (IsSuperUser | IsPartnerOwnerRole | IsPartnerMarketingSpecialistRole),
    #     "retrieve": (IsSuperUser | IsPartnerOwnerRole | IsPartnerMarketingSpecialistRole),
    #     "create": (IsSuperUser | IsPartnerOwnerRole | IsPartnerMarketingSpecialistRole),
    #     "update": (IsSuperUser | IsPartnerOwnerRole | IsPartnerMarketingSpecialistRole),
    #     "partial_update": (IsSuperUser | IsPartnerOwnerRole | IsPartnerMarketingSpecialistRole),
    # }

    @action(methods=["get"], detail=True, url_path="get-tasks")
    def get_tasks(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        project = self.get_object()
        queryset = project.tasks.all()

        serializer = self.get_serializer(queryset, many=True)
        return Response({"results": serializer.data})

