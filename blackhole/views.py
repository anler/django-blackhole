# -*- coding: utf-8 -*-

from .utils import get_template_response
from .decorators import patch_reverse


@patch_reverse
def view_template(request, name):
    """Render the template named ``name``"""
    return get_template_response(request, template_name=name)


@patch_reverse
def view_raw_template(request, name):
    """Render the template named `name` and return the response as `text/plain`"""
    return get_template_response(request, template_name=name, content_type="text/plain")
