#!/usr/bin/env python3
"""
this method return square of v and k
"""
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    return k and square v
    """
    return (k, float(v ** 2))
