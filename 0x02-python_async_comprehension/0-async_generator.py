#!/usr/bin/env python3
"""
A script that describe a coroutine with no arguments
"""

import asyncio
import random


async def async_generator() -> float:
    """
    A coroutine that loops 10 times, wait for 
    one second and output a random number
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
