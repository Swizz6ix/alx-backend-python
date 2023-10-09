#!/usr/bin/env python3

"""

"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Describes a function that executes multiple coroutines
    """
    tasks: List[int] = [wait_random(max_delay) for _ in range(n)]
    delay: List[int] = await asyncio.gather(*tasks)
    task_wait_random(max_delay)
    return sorted(delay)
