from django import http
from django.template import Template, RequestContext
from django.template.loader import get_template


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


def set_nested_keys(container, keys, value):
    """Recursively set a list of ``keys`` into a ``container``.

    Example:
        >>> c = {}
        >>> set_nested_keys(c, ['user', 'name'], 'my name'])
        >>> c
        {'user': {'name': 'my name'}}
    """
    key = keys[0]
    if len(keys) > 1:
        if key in container:
            new_container = container[key]
        else:
            new_container = {}
            container[key] = new_container
        set_nested_keys(new_container, keys[1:], value)
    else:
        container[key] = value


def nest_querydict(querydict):
    """Converts a querydict into a dict.

    If the querydict contains keys named like 'key1.key2=value', the result
    dict is gonna be nested:

        {
            'key1': {
                'key2': value
            }
        }

    :return: A dict with all keys and nested keys from the querydict.
    """
    container = {}
    for key, value in querydict.iteritems():
        set_nested_keys(container, key.split('.'), value)

    return container


@patch_reverse
def view_template(request, name):
    """Render the template named ``name``"""
    tpl = get_template(name)
    data = nest_querydict(request.GET)
    body = tpl.render(RequestContext(request, data))

    return http.HttpResponse(body)
