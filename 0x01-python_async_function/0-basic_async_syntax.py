#!/usr/bin/env python3 
"""
An async script that delay for a random seconds
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    An async function that delays for a random seconds

    Args:
        max_delay (int): The input seconds
    Returns:
        (float) in seconds
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
