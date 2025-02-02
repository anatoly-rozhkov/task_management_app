import uuid

from django.db import models

from apps.helpers import get_settings


class UUIDModel(models.Model):
    id = models.UUIDField("ID", default=uuid.uuid4, primary_key=True, editable=False)

    class Meta:
        abstract = True


class CreatedModel(models.Model):
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        abstract = True


class UpdatedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Named(models.Model):
    name = models.CharField(
        max_length=get_settings("DEFAULT_CHARFIELD_MAXLENGTH"),
        verbose_name="Name",
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name}"


class BaseUserStuff(models.Model):
    first_name = models.CharField("First name", max_length=128, blank=True, null=True)
    middle_name = models.CharField("Middle name", max_length=128, blank=True, null=True)
    last_name = models.CharField("Last name", max_length=128, blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        abstract = True
