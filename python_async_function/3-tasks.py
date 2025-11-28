#!/usr/bin/env python3
"""
this method return asyncio Task
"""


wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    create a asynico task
    """
    return asyncio.create_task(task_wait_random(max_delay))
