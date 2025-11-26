#!/usr/bin/env python3
"""
this method return sum of a list of float and int 
"""


from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """
    return list
    """
    return sum(mxd_lst)