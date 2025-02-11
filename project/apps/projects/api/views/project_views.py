import uuid
from django.db.models.query import QuerySet

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema, extend_schema_view

from apps.helpers.extended_viewsets import ReadCreateUpdateExtendedModelViewSet

from apps.projects.api.serializers import ProjectSerializer, ProjectListSerializer
from apps.projects.models import Project


@extend_schema_view(
    list=extend_schema(description="List all projects."),
    retrieve=extend_schema(description="Get project by id."),
    create=extend_schema(description="Create project."),
    update=extend_schema(description="Update project."),
    partial_update=extend_schema(description="Partially update project."),
)
class ProjectViewSet(ReadCreateUpdateExtendedModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    serializer_class_map = {
        "list": ProjectListSerializer,
        "retrieve": ProjectListSerializer,
        "create": ProjectSerializer,
        "update": ProjectSerializer,
        "partial_update": ProjectSerializer,
    }
    # permission_classes = (IsSuperUser,)
    # permission_classes_map = {
    #     "list": (IsSuperUser | IsPartnerOwnerRole | IsPartnerMarketingSpecialistRole),
    #     "retrieve": (IsSuperUser | IsPartnerOwnerRole | IsPartnerMarketingSpecialistRole),
    #     "create": (IsSuperUser | IsPartnerOwnerRole | IsPartnerMarketingSpecialistRole),
    #     "update": (IsSuperUser | IsPartnerOwnerRole | IsPartnerMarketingSpecialistRole),
    #     "partial_update": (IsSuperUser | IsPartnerOwnerRole | IsPartnerMarketingSpecialistRole),
    # }
