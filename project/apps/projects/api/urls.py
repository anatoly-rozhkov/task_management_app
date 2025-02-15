from rest_framework.routers import DefaultRouter

from apps.projects.api.views import ProjectViewSet, TaskViewSet

router = DefaultRouter()
router.register("projects", ProjectViewSet, "projects")
router.register("tasks", TaskViewSet, "tasks")
