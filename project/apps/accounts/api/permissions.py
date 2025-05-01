from typing import Any

from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import HttpRequest


class IsSuperUser(IsAuthenticated):
    def has_permission(self, request: HttpRequest, view: "views.APIView") -> bool:
        return bool(super().has_permission(request, view) and request.user.is_superuser)

    def has_object_permission(self, request: HttpRequest, view: "views.APIView", obj: Any) -> bool:
        return request.user.is_superuser
