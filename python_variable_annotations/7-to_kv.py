#!/usr/bin/env python3
"""
this method return square of v and k
"""


def to_kv(k: str, v: int | float) -> tuple[str, float]:
    """
    return k and square v
    """
    return (k, float(v ** 2))
