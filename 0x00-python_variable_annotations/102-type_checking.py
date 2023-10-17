#!/usr/bin/env python3

"""
A script that Uses mypy to validate the piece of code.
"""

from typing import Tuple, List

def zoom_array(lst: Tuple, factor: int=2) -> List:
    """
    A function that validate the typings of a code.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
