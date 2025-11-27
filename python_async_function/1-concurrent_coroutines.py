#!/usr/bin/env python3\
"""
Docstring for python_async_function.1-concurrent_coroutines
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


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
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        i = 0
        while i < len(delays) and delays[i] < delay:
            i += 1
        delays.insert(i, delay)

    return delays
