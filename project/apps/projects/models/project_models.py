from django.contrib.auth import get_user_model
from django.db import models

from apps.helpers.models import UUIDModel, Named, CreatedModel

User = get_user_model()


class Project(UUIDModel, Named, CreatedModel):
    description = models.TextField("Description", max_length=600)
    due_date = models.DateField("Due date")

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class Task(UUIDModel, Named, CreatedModel):
    project = models.ForeignKey(
        Project, verbose_name="Project", related_name="tasks", on_delete=models.CASCADE, null=True
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
