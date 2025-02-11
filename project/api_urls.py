from django.urls import include, path

from rest_framework import routers

from drf_spectacular.views import SpectacularRedocView, SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView
from apps.projects.api.urls import router as projects_router

router = routers.DefaultRouter()
router.registry.extend(projects_router.registry)


class TMSpectacularAPIView(SpectacularAPIView):
    patterns = [
        path("", include((router.urls, "api-root")), name="api-root"),
        # path("api/auth/obtain/", TokenObtainPairView.as_view(), name="auth_obtain_pair"),
        # path("api/auth/verify/", TokenVerifyView.as_view(), name="auth_verify"),
    ]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


urlpatterns = [
    # URL registration
    path("", include((router.urls, "api-root")), name="api-root"),
    # Auth
    # path("auth/obtain/", TokenObtainPairView.as_view(), name="auth_obtain_pair"),
    # path("auth/verify/", TokenVerifyView.as_view(), name="auth_verify"),
    # Swagger schema registration
    path("schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("schema-tm/", TMSpectacularAPIView.as_view(), name="schema-tm"),
    # Swagger schema
    path("schema/tm/swagger/", SpectacularSwaggerView.as_view(url_name="schema-tm"), name="swagger-tm-ui"),
    path("schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
