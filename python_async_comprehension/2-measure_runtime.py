#!/usr/bin/env python3
"""
coroutine that will execute async_comprehension
four times in parallel using asyncio.gather(*tasks)
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ return total time """
    start = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end = time.perf_counter()
    return end - start
