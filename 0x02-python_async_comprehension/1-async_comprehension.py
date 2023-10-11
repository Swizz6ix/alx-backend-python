#!/usr/bin/env python3
"""
A script that describe a coroutine that collects
10 random numbers
"""
import asyncio
from typing import List
from importlib import import_module as using
async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A function that returns a list of floats
    """
    return [num async for num in async_generator()]
