# -*- coding: utf-8 -*-
from django import http
from django.template import RequestContext
from django.template.loader import get_template

from .utils import nest_querydict
from .decorators import patch_reverse


@patch_reverse
def view_template(request, name):
    """Render the template named ``name``"""
    tpl = get_template(name)
    data = nest_querydict(request.GET)
    body = tpl.render(RequestContext(request, data))

    return http.HttpResponse(body)


@patch_reverse
def view_raw_template(request, *args, **kwargs):
    """Render the template named `name` and return the response as `text/plain`"""
    response = view_template(request, *args, **kwargs)
    response["Content-Type"] = "text/plain; charset=utf-8"
    return response
