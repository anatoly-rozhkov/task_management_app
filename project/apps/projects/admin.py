from django.contrib import admin

from apps.projects.models import Project, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    list_filter = ("name", "created_at")
    search_fields = ("id", "name")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    list_filter = ("name", "created_at")
    search_fields = ("id", "name")
