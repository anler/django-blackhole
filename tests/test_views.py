# -*- coding: utf-8 -*-
import pytest

@pytest.fixture
def client():
    from django.test.client import Client
    return Client()


def test_view_template(client):
    response = client.get('/templates/template.html/')

    assert '<p>template.html</p>\n' == response.content
    assert 'text/html' in response['content-type']


def test_view_nested_template(client):
    response = client.get('/templates/subdir/template.html/')

    assert '<p>subdir/template.html</p>\n' == response.content
    assert 'text/html; charset=utf-8' == response['content-type']


def test_view_raw_template(client):
    response = client.get('/templates/template.html/raw/')

    assert '<p>template.html</p>\n' == response.content
    assert 'text/plain; charset=utf-8' == response['content-type']


def test_view_template_with_mime(client):
    response = client.get('/templates/template.html/?_mime=text/plain')

    assert '<p>template.html</p>\n' == response.content
    assert 'text/plain; charset=utf-8' == response['content-type']
