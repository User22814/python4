import time
import requests
import threading
import multiprocessing
import asyncio
import aiohttp
import json


def measure(func):
    def wrap(*args, **kwargs):
        print('start measure')

        time1 = time.perf_counter()
        res = func(*args, **kwargs)  # ядро декорируемой функции

        print('end measure')
        print(f'функция потратила времени: {time.perf_counter() - time1}')
        return res

    return wrap


def download_json(name):
    response = requests.get(
        url="https://jsonplaceholder.typicode.com/todos/1",
        headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36'
        }
    )

    json_data = response.content.decode()

    with open(f'tmp/data_{name}.json', 'w') as file:
        json.dump(json_data, file)


@measure
def sync_f():
    for i in range(1, 11):
        download_json(i)


@measure
def threading_f():
    thread_list = [threading.Thread(target=download_json, args=(f"thread_{x}",), kwargs={}) for x in range(1, 11)]

    for i in thread_list:
        i.start()

    for i in thread_list:
        i.join()

    # exit


@measure
def processing_f():
    process_list = [multiprocessing.Process(target=download_json, args=(f"process_{x}",), kwargs={}) for x in
                    range(1, 11)]

    for i in process_list:
        i.start()

    for i in process_list:
        i.join()

    # exit


async def async_download_json(name):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url="https://jsonplaceholder.typicode.com/todos/1", headers=headers) as await_response:
            data = await await_response.read()

    with open(f'tmp/data_{name}.json', 'wb') as file:
        file.write(data)


@measure
def async_f():
    async def tasks_generator():  # корутины - coro  - задачи с задержкой по выполнению и возврату
        await asyncio.gather(
            *[async_download_json(f"async_{x}") for x in range(1, 11)]
        )

    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks_generator())


if __name__ == '__main__':  # точка входа, т.е. отсюда стартует этот файл при запуске
    sync_f()  # 59.278442899999995       1 thread * 1 process
    threading_f()  # 3.6611930999999998  1 * 100
    processing_f()  # 4.1108648          100 * 1
    async_f()  # 2.7549684                 1 * 1

# последовательно - 1 поток, 1 процесс (по очереди)
# многопоточно - N поток, 1 процесс
# мультипроцесс - N поток, N процесс
# асинхронно - 1 поток, 1 процесс (цикл событий)
