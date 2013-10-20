# -*- coding: utf-8 -*-


def patch_reverse(view):
    """Patch the default django's reverse function to return always `''`.
    This way you can test the templates without worrying about NoReverseMatch
    exceptions.
    """
    def decorator(*args, **kwargs):
        from django.core import urlresolvers

        reverse = urlresolvers.reverse
        urlresolvers.reverse = lambda *args, **kwargs: ''
        result = view(*args, **kwargs)
        urlresolvers.reverse = reverse

        return result
    return decorator
