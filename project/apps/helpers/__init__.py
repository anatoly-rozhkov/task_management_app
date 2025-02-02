from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def import_from_settings(attr, *args):
    """
    Load an attribute from the django settings.
    """
    try:
        if args:
            return getattr(settings, attr, args[0])
        return getattr(settings, attr)
    except AttributeError:
        raise ImproperlyConfigured("Setting {0} not found".format(attr))

def get_settings(attr, *args):
    return import_from_settings(attr, *args)