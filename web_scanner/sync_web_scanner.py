import time
from typing import Iterable

import requests


def sync_scan(urls: Iterable[str]) -> float:
    total_size = sum(len(requests.get(url).content) for url in urls)
    return total_size


if __name__ == '__main__':
    with open('web_scanner/urls.txt') as file:
        urls = [line.rstrip() for line in file]

    start = time.perf_counter()
    sync_scan(urls)
    print(f'Spend time = {time.perf_counter() - start:.2f}s')

