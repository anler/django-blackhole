# -*- coding: utf-8 -*-
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
