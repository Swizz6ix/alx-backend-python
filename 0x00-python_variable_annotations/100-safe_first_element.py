#!/usr/bin/env python3

"""
A script that accepts a sequence
"""

from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    A function that returns union of anything
    Args:
        Sequence
    """
    if lst:
        return lst[0]
    else:
        return None
