from rest_framework.routers import DefaultRouter

from apps.accounts.api.views import UserViewSet

router = DefaultRouter()
router.register("users", UserViewSet, "users")
