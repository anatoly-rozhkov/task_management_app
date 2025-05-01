from django.contrib.auth import get_user_model
from django.db.models.query import QuerySet

from rest_framework.permissions import IsAuthenticated, AllowAny

from drf_spectacular.utils import extend_schema, extend_schema_view

from rest_framework import status

from rest_framework.response import Response

from apps.accounts.api.permissions import IsSuperUser
from apps.accounts.api.serializers import UserSerializer, UserRetrieveSerializer, UserUpdateSerializer
from apps.helpers.extended_viewsets import FullExtendedModelViewSet

User = get_user_model()


@extend_schema_view(
    list=extend_schema(description="List all users."),
    retrieve=extend_schema(description="Get user by id."),
    create=extend_schema(description="Create user."),
    update=extend_schema(description="Update user."),
    partial_update=extend_schema(description="Partially update user."),
    destroy=extend_schema(description="Delete user."),
)
class UserViewSet(FullExtendedModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)
    permission_classes_map = {
        "list": IsAuthenticated,
        "retrieve": IsAuthenticated,
        "create": AllowAny,
        "update": IsAuthenticated,
        "partial_update": IsAuthenticated,
        "destroy": IsAuthenticated,
    }
    serializer_class_map = {
        "list": UserRetrieveSerializer,
        "retrieve": UserRetrieveSerializer,
        "create": UserSerializer,
        "update": UserUpdateSerializer,
        "partial_update": UserUpdateSerializer,
    }

    def get_queryset(self) -> "QuerySet[User]":
        queryset = super().get_queryset()
        if IsSuperUser().has_permission(self.request, self):
            return queryset
        else:
            return queryset.filter(id=self.request.user.id)

    def create(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_user = User.objects.create_user(**serializer.validated_data)
        response_serializer = UserRetrieveSerializer(new_user)
        # response_serializer.is_valid(raise_exception=True)

        return Response(
            response_serializer.data, status=status.HTTP_201_CREATED, headers=self.get_success_headers(serializer.data)
        )
