# -*- coding: utf-8 -*-
import os
import json

from collections import defaultdict

from django.template.response import TemplateResponse
from django.db.models import get_apps
from django.utils.six import iteritems


def set_nested_keys(container, keys, value):
    """Recursively set a list of ``keys`` into a ``container``.

    :param container: The container dict.
    :param keys: List of keys to nest.
    :param value: Value to set to the deepest nested key.

    Example:
    >>> c = {}
    >>> set_nested_keys(c, ['user', 'name'], 'my name')
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

    Multi-value values are converted into nested dicts, that is, if the querydict contains keys
    named like 'key1.key2=value', the result dict is gonna be nested:

    {
        'key1': {
            'key2': value
        }
    }

    :return: A dict with all keys and nested keys from the querydict.
    """
    container = {}
    for key, value in iteritems(querydict):
        set_nested_keys(container, key.split('.'), value)

    return container


def combine_content_type_and_charset(content_type, charset):
    if not content_type:
        content_type = "text/html"
    if not charset:
        charset = "utf-8"
    if "charset" not in content_type:
        content_type = "{}; charset={}".format(content_type, charset)
    return content_type


def get_options(data):
    def is_option(option):
        return option.startswith("_")
    return defaultdict(str, {k: v for k, v in iteritems(data) if is_option(k)})


def get_fixture_path(fixture):
    app_module_paths = []
    for app in get_apps():
        if hasattr(app, '__path__'):
            for path in app.__path__:
                app_module_paths.append(path)
        else:
            app_module_paths.append(app.__file__)

    app_fixtures = (os.path.join(os.path.dirname(path), 'fixtures') for path in app_module_paths)
    join, isfile = os.path.join, os.path.isfile
    for fixtures_path in app_fixtures:
        abs_fixture_path = "{}.json".format(join(fixtures_path, fixture))
        if isfile(abs_fixture_path):
            return abs_fixture_path


def load_fixture(fixture):
    data = {}
    if fixture:
        fixture_path = get_fixture_path(fixture)
        if fixture_path:
            data.update(json.load(open(fixture_path)))
    return data


def get_template_response(request, template_name, content_type=None, charset=None):
    """Get a template content rendered with data from request return a response.

    :param request: Django's request object.
    :param template_name: Name of the template to render.
    :param content_type: Content type of the response. Default is "text/html" if
    `request.GET['_mime']` is not found.
    :param charset: Charset of the response. Default is "utf-8" if `request.GET['_charset']` is not
    found.

    :return: :class:`~django.template.response.TemplateResponse` instance.
    """
    default_options = get_options(request.GET)
    data = nest_querydict(request.GET)
    data.update(load_fixture(default_options['_fixture']))

    if content_type is None:
        content_type = default_options['_mime']
    if charset is None:
        charset = default_options['_charset']
    content_type = combine_content_type_and_charset(content_type, charset)

    return TemplateResponse(request, template_name, data, content_type=content_type)
