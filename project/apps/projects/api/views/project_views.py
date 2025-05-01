from django.db.models import QuerySet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from rest_framework.response import Response

from drf_spectacular.utils import extend_schema, extend_schema_view

from apps.accounts.api.permissions import IsSuperUser
from apps.helpers.extended_viewsets import FullExtendedModelViewSet

from apps.projects.api.serializers import ProjectSerializer, ProjectListSerializer
from apps.projects.models import Project


@extend_schema_view(
    list=extend_schema(description="List all projects."),
    retrieve=extend_schema(description="Get project by id."),
    create=extend_schema(description="Create project."),
    update=extend_schema(description="Update project."),
    partial_update=extend_schema(description="Partially update project."),
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
    }
    permission_classes = (IsSuperUser,)
    permission_classes_map = {
        "list": IsAuthenticated,
        "retrieve": IsAuthenticated,
        "create": IsAuthenticated,
        "update": IsAuthenticated,
        "partial_update": IsAuthenticated,
        "destroy": IsAuthenticated,
    }

    def get_queryset(self) -> QuerySet[Project]:
        queryset = super().get_queryset()
        if IsSuperUser().has_permission(self.request, self):
            return queryset
        else:
            return queryset.filter(user=self.request.user.id)

    def create(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.validated_data["user"] = request.user
        serializer.save()

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=self.get_success_headers(serializer.data)
        )
