#!/usr/bin/env python3
"""
Module that provides a function to sum a list of ints and floats.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing ints and floats.
    """
    return sum(mxd_lst)
