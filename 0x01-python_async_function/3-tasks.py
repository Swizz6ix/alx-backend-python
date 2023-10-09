#!/usr/bin/env python3
"""
A script that returns asyncio.Task
"""

import asyncio
from asyncio import Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Describe a function that returns asyncio.Task
    """
    return asyncio.Task(wait_random(max_delay))
