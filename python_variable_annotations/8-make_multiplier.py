#!/usr/bin/env python3
"""
takes a float multiplier as argument and returns a function that multiplies
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    return a function that multiplies a float
    """
    def multiply(value: float) -> float:
        return value * multiplier
    return multiply
