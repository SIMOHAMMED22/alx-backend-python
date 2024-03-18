#!/usr/bin/env python3


import asyncio
import random


async def wait_random(max_delay=10):
    """
    Asynchronously waits for a random amount of time
                            between 0 and `max_delay` seconds.

    :param max_delay: A float representing the maximum
                                        amount of time to wait. Defaults to 10.
    :type max_delay: float

    :return: A float representing the amount of time waited.
    :rtype: float
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
