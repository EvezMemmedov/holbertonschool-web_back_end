#!/usr/bin/env python3
"""
Docstring for python_async_function.1-concurrent_coroutines
"""


from wait_random import wait_random
from typing import List
import asyncio


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Docstring for wait_n
    :param n: Description
    :type n: int
    :param max_delay: Description
    :type max_delay: int
    :return: Description
    :rtype: List[float]
    """
    task = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for tsk in asyncio.as_completed(task):
        delay = await tsk
        i = 0
        while i < len(delays) and delays[i] < delay:
            i += 1
        delays.insert(i, delay)
    return delays
