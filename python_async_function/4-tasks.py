#!/usr/bin/env python3
"""
execute multiple async tasks
"""


import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """
    return sort delay
    """
    tasks = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)
        delay = await asyncio.gather(*tasks)
        return sorted(delay)
