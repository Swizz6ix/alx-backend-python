#!/usr/bin/env python3

"""
A script that returns a tuple from a string and int or float
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    A function that takes a string and integer or float as argument and return a tuple

    Args:
        K (str): The first argument
        v (Union[int, float]) : The second argument that can either be an integer or a float

    Returns:
        Tuple(str, float): returns a tuple of type string and float
    """
    return (k, v * v)
