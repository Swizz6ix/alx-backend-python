#!/usr/bin/env python
"""
A script that describe a coroutine that collects 
10 random numbers
"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A function that returns a list of floats
    """
    return [num async for num in async_generator()]
