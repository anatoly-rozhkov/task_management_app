from rest_framework import serializers

from rest_framework_simplejwt.serializers import RefreshToken, TokenRefreshSerializer


class ExtendedTokenRefreshSerializerSerializer(TokenRefreshSerializer):
    refresh = serializers.CharField()
    access = serializers.CharField(read_only=True)
    token_class = RefreshToken

    def validate(self, attrs):
        refresh = self.token_class(attrs["refresh"])
        attrs["refresh"] = str(refresh)

        return super().validate(attrs)
