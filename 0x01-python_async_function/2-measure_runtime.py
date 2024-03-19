#!/usr/bin/env python3
"""This module contains the function"""
import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Calculate the average time taken to run the wait_n function
                                        with the given parameters.

    Parameters:
    - n (int): The number of times to run the wait_n function.
    - max_delay (int): The maximum delay for each run of the wait_n function.

    Returns:
    - float: The average time taken per run of the wait_n function.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
