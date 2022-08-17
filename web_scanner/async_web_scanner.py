import asyncio
import time
from typing import Iterable

import aiohttp as aiohttp


async def async_get(session, url: str):
    async with session.get(url) as response:
        content = await response.read()
        print(f'[{url}] completed')
        return content


async def async_scan(urls: Iterable[str]) -> float:
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(async_get(session, url)) for url in urls]
        responses = await asyncio.gather(*tasks)
        return sum(map(len, responses))


if __name__ == '__main__':
    with open('urls.txt') as file:
        urls = [line.rstrip() for line in file]

    start = time.perf_counter()
    asyncio.run(async_scan(urls))
    print(f'Spend time = {time.perf_counter() - start:.2f}s')
