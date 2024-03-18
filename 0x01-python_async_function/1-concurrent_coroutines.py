#!/usr/bin/env python3
"""This module contains the function"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    A function that waits for 'n' random delays with
                            a maximum delay of 'max_delay'.

    :param n: An integer representing the number of delays to wait for.
    :param max_delay: An integer representing the maximum delay time.
    :return: A sorted list of delays.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
