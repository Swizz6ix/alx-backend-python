#!/usr/bin/env python3
"""
A script that execute multiple coroutines at the same time with async
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Describes a function that executes multiple coroutines
    """
    tasks: List[int] = [wait_random(max_delay) for _ in range(n)]
    delay: List[int] = await asyncio.gather(*tasks)
    return sorted(delay)
