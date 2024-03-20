#!/usr/bin/env python3
"""Async Generator"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]: # type: ignore
    """
    An asynchronous generator that yields random integers between
                    0 and 10 after sleeping for 1 second each time.
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)


async def main():
    async for number in async_generator():
        print(number)
