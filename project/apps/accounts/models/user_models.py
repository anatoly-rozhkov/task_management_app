import logging
from typing import Any, List, Optional

from django.contrib.auth import models as auth_models
from django.db import models

from apps.helpers.models import CreatedModel, UUIDModel

logger = logging.getLogger(__name__)


class UserManager(auth_models.UserManager):
    use_in_migrations = True

    def _create_user(self, email: str, password: Optional[str], **extra_fields: Any) -> Any:
        """
        Create and save a user with the given email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, password: Optional[str] = None, **extra_fields: Any) -> Any:
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email: str, password: Optional[str] = None, **extra_fields: Any) -> Any:
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(auth_models.AbstractUser, UUIDModel, CreatedModel):
    email = models.EmailField("email address", unique=True)
    username = None
    USERNAME_FIELD = "email"
    objects = UserManager()
    REQUIRED_FIELDS: List[str] = []

    class Meta(auth_models.AbstractUser.Meta):
        ordering = ("-date_joined",)
        swappable = "AUTH_USER_MODEL"
        verbose_name = "User"
        verbose_name_plural = "Users"
        indexes = (models.Index(fields=("email",)),)

    def __str__(self) -> str:
        full_name = self.get_full_name()
        if full_name:
            return full_name + f" ({self.email})"
        else:
            return str(self.email)

    @classmethod
    def get_lowercased_class_name(cls):
        return cls._meta.model_name

    @property
    def get_short_name(self) -> str:
        return (
            f"{self.last_name} {self.first_name[:1] if self.first_name else ''}."
            + f"{self.middle_name[:1] if self.middle_name else ''}.".strip()
        )
