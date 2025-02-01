import mimetypes
import posixpath
from pathlib import Path

from django.http.response import FileResponse, Http404, HttpResponseNotModified
from django.utils._os import safe_join
from django.utils.http import http_date
from django.utils.translation import gettext_lazy as _
from django.views.static import directory_index, was_modified_since

from rest_framework.request import Request


def serve(request: Request, path, document_root=None, show_indexes=False, force_download=False):  # type: ignore
    download = request.GET.get("download", False) or force_download
    path = posixpath.normpath(path).lstrip("/")
    fullpath = Path(safe_join(document_root, path))
    if fullpath.is_dir():
        if show_indexes:
            return directory_index(path, fullpath)
        raise Http404(_("Directory indexes are not allowed here."))
    if not fullpath.exists():
        raise Http404(_("“%(path)s” does not exist") % {"path": fullpath})
    # Respect the If-Modified-Since header.
    statobj = fullpath.stat()
    if not download and not was_modified_since(
        request.META.get("HTTP_IF_MODIFIED_SINCE"), statobj.st_mtime, statobj.st_size
    ):
        return HttpResponseNotModified()
    content_type, encoding = mimetypes.guess_type(str(fullpath))
    content_type = content_type or "application/octet-stream"
    response = FileResponse(fullpath.open("rb"), filename=fullpath.name, content_type=content_type)
    response["Last-Modified"] = http_date(statobj.st_mtime)
    if download:
        response["Content-Disposition"] = "attachment"
    if encoding:
        response["Content-Encoding"] = encoding
    return response
