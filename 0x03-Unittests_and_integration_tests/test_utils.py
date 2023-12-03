#!/usr/bin/env python3
"""
This module contains unittest test for utils module
"""
import unittest
from typing import Dict, Tuple, Union, Mapping, Sequence, Any, Callable
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    The test fixture for testing the access_nested_map method
    in the utils modules
    """
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    def test_access_nested_map(self,
                                nested_map: Mapping,
                                path: Sequence,
                                expected: Union[Dict, int]
                            ) -> None:
        """
        Test the method access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand({
        ({}, ('a',), KeyError),
        ({'a': 1}, ('a', 'b'), KeyError)
    })
    def test_access_nested_map_exception(
        self,
        nested_map: Dict,
        path: Tuple[str],
        exception: Exception,
    ) -> None:
        """
        test access nested map for exception
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """
    The test fixture for testing get_json method in utils module.
    """
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http//holberton.io', {'payload': False}),
    ])
    def test_get_json(
        self,
        test_url: str,
        test_payload: Dict,
    ) -> None:
        """
        test for json
        """
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)

class TestMemoize(unittest.TestCase):
    """
    The test fixture fir testing memoize method in util module.
    """
    def test_memoize(self) -> None:
        """
        Test the memoize function
        """
        class TestClass:
            def a_method(self):
                return 42
            
            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
            TestClass,
            'a_method',
            return_value = lambda: 42,
        ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()
