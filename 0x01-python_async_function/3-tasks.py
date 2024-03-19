#!/usr/bin/env python3
"""This module contains the function"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    A function that creates a new asyncio task that waits for a random
                        amount of time within the specified 'max_delay'
                        and returns the created task.

    Parameters:
    - max_delay: an integer representing the maximum delay for waiting.

    Returns:
    - asyncio.Task: a new asyncio task that waits for a random amount of
            time within the specified 'max_delay'.
    """

    task = asyncio.create_task(wait_random(max_delay))
    return task
