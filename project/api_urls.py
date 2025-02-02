from django.urls import include, path

from rest_framework import routers

from drf_spectacular.views import SpectacularRedocView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

router = routers.DefaultRouter()

urlpatterns = [
    # URL registration
    path("", include((router.urls, "api-root")), name="api-root"),
    # Auth
    path("auth/obtain/", TokenObtainPairView.as_view(), name="auth_obtain_pair"),
    path("auth/verify/", TokenVerifyView.as_view(), name="auth_verify"),
    # Swagger schema registration
    path("schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
