#!/usr/bin/env python3
"""1-async_comprehension.py second task"""

import asyncio
import random

async_generator = __import__("0-async_generator").async_generator

async def async_comprehension():
    """coroutine collect 10 random nubmbers.
       from async_generator"""
    result = [i async for i in async_generator()]
    return result