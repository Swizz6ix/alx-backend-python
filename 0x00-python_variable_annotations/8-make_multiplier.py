#!/usr/bin/env python3

"""
A script that defines a function to create a multiplier function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function
    Args:
        multiplier (float): The multiplier float number

    Returns:
        Callable[[float], float]: A function that multiplies
        a float by the specified multiplier.
    """

    def multiplier_function(x: float) -> float:
        """
        Multiply a float by the specified multiplier

        Args:
            x (float): the float number argument

        Returns:
            float: The result of multiplying x by the multiplier
        """
        return x * multiplier
    return multiplier_function
