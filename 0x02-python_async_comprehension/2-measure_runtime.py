#!/usr/bin/env python3
"""2-measure_runtime.py third task"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension

async def measure_runtime():
    """measure time of asyincing four.
       async_comprehension parallel"""
    start = time.time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    end = time.time()
    return end - start