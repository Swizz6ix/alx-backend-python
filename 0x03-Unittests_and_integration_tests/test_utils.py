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
    def test_access_nested_map(
        self,
        nested_map: Mapping,
        path: Sequence,
        expected: Union[Dict, int]
    ) -> None:
        """
        Test the method access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',)),
        ({'a': 1}, ('a', 'b'))
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Mapping,
        path: Sequence,
    ) -> None:
        """
        test access nested map for exception
        """
        with self.assertRaises(KeyError, mgs=path):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    The test fixture for testing get_json method in utils module.
    """
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False}),
    ])
    def test_get_json(
        self,
        test_url: str,
        test_payload: Dict,
    ) -> None:
        """
        test for json
        """
        mock_obj = Mock()
        mock_obj.json.return_value = test_payload
        with patch("requests.get", return_value=mock_obj) as mock_req_get:
            self.assertEqual(get_json(test_url), test_payload)
            mock_req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    The test fixture fir testing memoize method in util module.
    """
    def test_memoize(self) -> None:
        """Test the memoize function"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
            TestClass,
            'a_method',
        ) as patch_obj:
            patch_obj.return_value = 42
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            patch_obj.assert_called_once()
