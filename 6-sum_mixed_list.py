#!/usr/bin/env python3

"""
A script that takes a list made of both integers and floats, sum them up and the result as float
"""

from typing import Union

def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    """
    A function returns a float from the sum of a list which is made up of both integers and floats

    Args:
        mxd_lst: Union[int, float]: the mixed list of both integers and floats

    Returns:
        float: the sum of all the integers and floats numbers in the list
    """
    sum: float = 0.0
    for num in mxd_lst:
        sum += num
    return sum
