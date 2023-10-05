#!/usr/bin/env python3 

"""
A script which takes of floats as argument and return their sum
"""

def sum_list(input_list: list[float]) -> float:
    """
    A function that takes a list of float numbers as argument and return their sum as float

    Args:
        input-list: list[float]: list od float numbers

    Returns:
        float: sum of all the float numbers in the list
    """
    sum: float = 0.0
    for num in input_list:
        sum += num
    return sum