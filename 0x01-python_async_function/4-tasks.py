#!/usr/bin/env python3
"""This module contains the function"""
import asyncio
from random import uniform
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for a specific number of tasks to
                            complete with a maximum delay.

    Parameters:
        n (int): The number of tasks to wait for.
        max_delay (float): The maximum delay in seconds for each task.

    Returns:
        List[float]: A sorted list of delays for each completed task.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
