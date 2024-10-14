#!/usr/bin/env python3
"""alx-backend-python/0x01-python_async_function/3-tasks.py"""

import asyncio
from asyncio import Task

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Import wait_random from 0-basic_async_syntax.

    Write a function (do not create an async function, use the regular function syntax to do this) task_wait_random that takes an integer max_delay and returns a asyncio.Task.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
