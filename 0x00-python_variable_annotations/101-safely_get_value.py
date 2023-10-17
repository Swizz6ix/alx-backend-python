#!/usr/bin/env python3
"""
A script that returns a Union
"""

from typing import Mapping, Any, Union, TypeVar


# Define a type variable ~T
T = TypeVar('T')
unionT = Union[T, None]
unionAny = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: unionT = None) -> unionAny:
    """
    A function that accepts Mapping
    """
    if key in dct:
        return dct[key]
    else:
        return default
