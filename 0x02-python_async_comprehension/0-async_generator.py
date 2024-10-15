#!/usr/bin/env python3
"""0-async_generator.py first task"""

import asyncio
import random

async def async_generator():
    """coroutine well run 10 times.
       each time well wait one second then
       yield a random num"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
    
