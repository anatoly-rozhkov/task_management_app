from .common import *  # noqa
from .links import *  # noqa

SITE_URL = "http://localhost:8000"
ALLOWED_HOSTS = ["*"]
DEBUG = True
SECRET_KEY = "not-a-valid-secret-key"

MIDDLEWARE.append(
    "livereload.middleware.LiveReloadScript",
)

INSTALLED_APPS += ("livereload",)
INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]
