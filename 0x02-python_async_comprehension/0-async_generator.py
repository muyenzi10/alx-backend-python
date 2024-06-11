#!/usr/bin/env python3
""" Corouting """

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """ Looping """

    for i in range(10):
        yield random.random()
        await asyncio.sleep(1)
