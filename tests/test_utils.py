# -*- coding: utf-8 -*-
import mock

from django.http import QueryDict

from blackhole.utils import nest_querydict, set_nested_keys


class TestSetNestedKeys:
    def test_one_key(self):
        container = {}
        key = "somekey"
        value = "somevalue"
        set_nested_keys(container, [key], value)

        assert container[key] == value
        assert list(container.keys()) == [key]

    def test_two_keys(self):
        container = {}
        key1, key2 = "somekey1", "somekey2"
        value = "somevalue"
        set_nested_keys(container, [key1, key2], value)

        assert container[key1][key2] == value
        assert list(container.keys()) == [key1]

    def test_three_keys(self):
        container = {}
        key1, key2, key3 = "somekey1", "somekey2", "somekey3"
        value = "somevalue"
        set_nested_keys(container, [key1, key2, key3], value)

        assert container[key1][key2][key3] == value
        assert list(container.keys()) == [key1]


@mock.patch("blackhole.utils.set_nested_keys")
class TestNestQuerydict:
    def test_one_key(self, set_nested_keys):
        querydict = QueryDict("somekey=somevalue")
        nest_querydict(querydict)
        set_nested_keys.assert_called_once_with({}, ["somekey"], "somevalue")

    def test_two_keys(self, set_nested_keys):
        querydict = QueryDict("somekey1=somevalue&somekey2=somevalue")
        nest_querydict(querydict)

        expected = [mock.call({}, ["somekey2"], "somevalue"),
                    mock.call({}, ["somekey1"], "somevalue")]

        assert set_nested_keys.call_args_list == expected

    def test_two_nested_keys(self, set_nested_keys):
        querydict = QueryDict("somekey1.somekey2=somevalue")
        nest_querydict(querydict)

        set_nested_keys.assert_called_once_with({}, ["somekey1", "somekey2"], "somevalue")
