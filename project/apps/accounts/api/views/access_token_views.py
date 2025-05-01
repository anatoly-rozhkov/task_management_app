from rest_framework_simplejwt.views import TokenRefreshView

from apps.accounts.api.serializers import ExtendedTokenRefreshSerializerSerializer


class ExtendedTokenRefreshView(TokenRefreshView):
    serializer_class = ExtendedTokenRefreshSerializerSerializer


token_obtain_pair = TokenRefreshView.as_view()
