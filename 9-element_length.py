#!/usr/bin/env python3

"""
This script defines a function to calculate the lengths of Sequences in an iterable
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    calculate the lengths of sequences in an iterable

    Args:
        lst (Iterable[Sequence]): An iterable containing sequence (eg., lists, strings)

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing a sequence and its length
    """
    return [(i, len(i)) for i in lst]