#!/usr/bin/env python3
"""
Async Comprehensions
"""
from typing import List
Vector = List[float]

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Vector:
    """
    Coroutine async_comprehension
    """
    stop = [y async for y in async_generator()]
    return stop
