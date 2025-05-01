from typing import Any, Dict

from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.validators import UniqueValidator


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="Specified email is already linked with another user",
            )
        ],
    )

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "password",
        )
        read_only_fields = ("id",)

    # def validate_email(self, value):
    #     user = self.context["request"].user
    #     if user.email == value:
    #         raise serializers.ValidationError("This email is already linked with your account")
    #     return value

    # def get_permissions(self, obj: Any) -> Dict[str, Dict[str, bool]]:
    #     from api_urls import router
    #
    #     resources = {}
    #
    #     for route in router.registry:
    #         actions = ["list", "create", "retrieve", "update", "partial_update", "delete"] + [
    #             action.__name__ for action in route[1].get_extra_actions()
    #         ]
    #         allowed_actions = {}
    #         for action in actions:
    #             view = route[1](request=self.context["request"], action=action)
    #
    #             if view.get_permissions()[0].has_permission(self.context["request"], self):
    #                 allowed_actions[action] = True
    #         resources[route[0]] = allowed_actions
    #
    #     return resources


class UserUpdateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=False,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="This email address is already in use. Please supply a different email address.",
            )
        ],
    )

    class Meta:
        model = User
        fields = (
            "id",
            "email",
        )
        read_only_fields = ("id",)


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
        )
        read_only_fields = ("id", "email", "first_name", "last_name")
