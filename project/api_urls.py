from django.urls import include, path

from rest_framework import routers

from drf_spectacular.views import SpectacularRedocView, SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

from apps.accounts.api.views.access_token_views import ExtendedTokenRefreshView
from apps.projects.api.urls import router as projects_router
from apps.accounts.api.urls import router as accounts_router

router = routers.DefaultRouter()
router.registry.extend(projects_router.registry)
router.registry.extend(accounts_router.registry)


class TMSpectacularAPIView(SpectacularAPIView):
    patterns = [
        path("api/", include((router.urls, "api-root")), name="api-root"),
        path("api/auth/obtain/", TokenObtainPairView.as_view(), name="auth_obtain_pair"),
        path("api/auth/refresh/", ExtendedTokenRefreshView.as_view(), name="auth_refresh"),
        path("api/auth/verify/", TokenVerifyView.as_view(), name="auth_verify"),
    ]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


urlpatterns = [
    # URL registration
    path("", include((router.urls, "api-root")), name="api-root"),
    # Auth
    path("auth/obtain/", TokenObtainPairView.as_view(), name="auth_obtain_pair"),
    path("auth/refresh/", ExtendedTokenRefreshView.as_view(), name="auth_refresh"),
    path("auth/verify/", TokenVerifyView.as_view(), name="auth_verify"),
    # Swagger schema registration
    path("schema-tm/", TMSpectacularAPIView.as_view(), name="schema-tm"),
    # Swagger schema
    path("schema/tm/swagger/", SpectacularSwaggerView.as_view(url_name="schema-tm"), name="swagger-tm-ui"),
    path("schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
