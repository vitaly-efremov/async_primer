import pathlib
import time
from concurrent.futures import ThreadPoolExecutor
from typing import Iterable

import requests


def get_response(url):
    response = requests.get(url)
    print(f'[{url}] completed')
    return response.content


def thread_scan(urls: Iterable[str]) -> float:
    with ThreadPoolExecutor() as thread_executor:
        responses = thread_executor.map(get_response, urls)

    total_size = sum(map(len, responses))
    return total_size


if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.resolve()
    with open(path.joinpath('urls.txt')) as file:
        urls = [line.rstrip() for line in file]

    start = time.perf_counter()
    thread_scan(urls)
    print(f'Spent time = {time.perf_counter() - start:.2f}s')

