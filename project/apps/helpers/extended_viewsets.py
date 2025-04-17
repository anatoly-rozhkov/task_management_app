from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from drf_extended_viewset import ExtendViewSet


class ReadUpdateDestroyViewSet(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet
):
    """
    A viewset that provides default `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """

    pass


class CreateDestroyViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    """
    A viewset that provides default `create()` and `destroy()` actions.
    """

    pass


class ReadUpdateViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, GenericViewSet):
    """
    A viewset that provides default `retrieve()`, `update()`,
    `partial_update()` and `list()` actions.
    """

    pass


class ReadUpdateExtendedModelViewSet(ExtendViewSet, ReadUpdateViewSet):
    """
    Examples:
    class MyModelViewSet(ReadUpdateExtendedModelViewSet):
        serializer_class_map = {
            'list': ListMyModelSerializer,
            'retrieve': RetrieveMyModelSerializer,
            'update': UpdateMyModelSerializer,
            'partial_update': UpdateMyModelSerializer,
        }
        permission_classes_map = {
            'list': AllowAny,
            'retrieve': IsAuthenticated,
            'update': (IsOwner | IsAdminUser),
            'partial_update': (IsOwner | IsAdminUser),
        }
    """

    pass


class ReadExtendedModelViewSet(ExtendViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """
    Examples:
    class MyModelViewSet(ReadExtendedModelViewSet):
        serializer_class_map = {
            'list': ListMyModelSerializer,
            'retrieve': RetrieveMyModelSerializer,
            'update': UpdateMyModelSerializer,
            'partial_update': UpdateMyModelSerializer,
        }
        permission_classes_map = {
            'list': AllowAny,
            'retrieve': IsAuthenticated,
            'update': (IsOwner | IsAdminUser),
            'partial_update': (IsOwner | IsAdminUser),
        }
    """

    pass


class ReadUpdateDestroyExtendedModelViewSet(ExtendViewSet, ReadUpdateDestroyViewSet):
    """
    Examples:
    class MyModelViewSet(ReadUpdateDestroyExtendedModelViewSet):
        serializer_class_map = {
            'list': ListMyModelSerializer,
            'retrieve': RetrieveMyModelSerializer,
        }
        permission_classes_map = {
            'list': AllowAny,
            'retrieve': IsAuthenticated,
        }
    """

    pass


class EmptyExtendedViewSet(ExtendViewSet, GenericViewSet):
    """
    Examples:
    class MyModelViewSet(EmptyExtendedViewSet):
        serializer_class_map = {}
        permission_classes_map = {}
    """

    pass


class RUExtendedModelViewSet(
    ExtendViewSet,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    pass


class ReadCreateExtendedModelViewSet(
    ExtendViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet
):
    """
        Examples:
    class MyModelViewSet(ReadCreateExtendedModelViewSet):
        serializer_class_map = {
            'list': ListMyModelSerializer,
            'retrieve': RetrieveMyModelSerializer,
            'create': CreateMyModelSerializer,
        }
        permission_classes_map = {
            'list': AllowAny,
            'retrieve': IsAuthenticated,
            'create': (IsOwner | IsAdminUser),
        }
    """

    pass

class FullExtendedModelViewSet(ReadCreateExtendedModelViewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """
        Examples:
    class MyModelViewSet(FullExtendedModelViewSet):
        serializer_class_map = {
            'list': ListMyModelSerializer,
            'retrieve': RetrieveMyModelSerializer,
            'update': UpdateMyModelSerializer,
            'create': CreateMyModelSerializer,
            'destroy': DestroyMyModelSerializer,
        }
        permission_classes_map = {
            'list': AllowAny,
            'retrieve': IsAuthenticated,
            'update': (IsOwner | IsAdminUser),
            'create': (IsOwner | IsAdminUser),
            'destroy': (IsOwner | IsAdminUser),
        }
    """

    pass

class ReadCreateUpdateExtendedModelViewSet(ReadCreateExtendedModelViewSet, mixins.UpdateModelMixin):
    """
        Examples:
    class MyModelViewSet(ReadCreateUpdateExtendedModelViewSet):
        serializer_class_map = {
            'list': ListMyModelSerializer,
            'retrieve': RetrieveMyModelSerializer,
            'update': UpdateMyModelSerializer,
            'create': CreateMyModelSerializer,
        }
        permission_classes_map = {
            'list': AllowAny,
            'retrieve': IsAuthenticated,
            'update': (IsOwner | IsAdminUser),
            'create': (IsOwner | IsAdminUser),
        }
    """

    pass


class CreateDestroyExtendedModelViewSet(ExtendViewSet, CreateDestroyViewSet):
    """
        Examples:
    class MyModelViewSet(CreateDestroyExtendedModelViewSet):
        serializer_class_map = {
            'create': CreateMyModelSerializer,
        }
        permission_classes_map = {
            'create': (IsOwner | IsAdminUser),
            'destroy': (IsOwner | IsAdminUser),
        }
    """

    pass
