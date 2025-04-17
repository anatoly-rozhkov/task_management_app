from typing import List, Union

from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, reverse_lazy
from django.urls.resolvers import URLPattern, URLResolver
from django.views.generic import RedirectView

from apps.helpers.static import serve

urlpatterns: List[Union[URLPattern, URLResolver]] = [
    path("", RedirectView.as_view(url=reverse_lazy("admin:index"))),
    path("admin/", admin.site.urls),
    path("api/", include(("api_urls", None))),
]


if settings.SILK_PROFILING:
    urlpatterns += [
        path(f"{settings.SILK_PANEL_PREFIX}/", include("silk.urls", namespace="silk")),
    ]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.views import debug

    urlpatterns.append(path("", debug.default_urlconf))
    urlpatterns.append(path("api-auth/", include("rest_framework.urls")))
    urlpatterns.extend(static(settings.MEDIA_URL, view=serve, document_root=settings.MEDIA_ROOT))
