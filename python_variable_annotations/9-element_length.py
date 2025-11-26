#!/usr/bin/env python3
"""
Module that provides a function to return the length of each element in an iterable.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing
    """
    return [(i, len(i)) for i in lst]
