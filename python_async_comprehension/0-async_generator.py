#!/usr/bin/env python3
""" coroutine will loop 10 times,
each time asynchronously wait 1 second
"""


import asyncio
import random
import typing


async def async_generator() -> typing.AsyncGenerator[float, None]:
    """
    yield a random number between 0 and 10
    """
    for i in range (10):
        await asyncio.sleep(1)
        yield random.random() * 10
