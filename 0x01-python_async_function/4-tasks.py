#!/usr/bin/env python3
"""alx-backend-python/0x01-python_async_function/4-tasks.py"""

import asyncio
from typing import List

wait_n = __import__("1-concurrent_coroutines").wait_n
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Take the code from wait_n and alter it into
    a new function task_wait_n. The code is nearly
    identical to wait_n except task_wait_random is
    being called.
    """
    tasks = []
    for times in range(n):
        tasks.append(task_wait_random(max_delay))
    return [await task for task in asyncio.as_completed(tasks)]
