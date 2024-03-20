#!/usr/bin/env python3
""" Async Comprehensions """

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously comprehends a list of numbers
                        generated by an async generator.

    Returns:
        A list of numbers generated by the async generator.
    """
    numbers = [number async for number in async_generator()]
    return numbers