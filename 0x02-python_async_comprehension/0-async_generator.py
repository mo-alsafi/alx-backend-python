#!/usr/bin/env python3
"""0-async_generator.py first task"""

import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """coroutine well run 10 times.
       each time well wait one second then
       yield a random num"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
    
