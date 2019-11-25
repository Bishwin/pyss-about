import asyncio

@asyncio.coroutine
def py34_coro():
    """Generator-based coroutine, older syntax"""
    yield from stuff()


async def py35_coro():
    """Native coroutine, modern syntax"""
    await stuff()

