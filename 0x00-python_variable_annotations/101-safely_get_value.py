#!/usr/bin/env python3
"""
A script that returns a Union
"""

from typing import Mapping, Any, Union, TypeVar


# Define a type variable ~T
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
    Union[T, None] = None) -> Union[Any, T]:
    """
    A function that accepts Mapping
    """
    if key in dct:
        return dct[key]
    else:
        return default
