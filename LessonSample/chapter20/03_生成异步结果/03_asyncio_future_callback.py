import asyncio
import functools
import time

def callback(future, n):
    print('future{}完成，结果: {}'.format(n, future.result()))


async def register_callbacks(all_done):
    #这些函数会在结果被设置时调用，调用顺序通注册顺序
    print('在future中注册callbacks')
    all_done.add_done_callback(functools.partial(callback, n='A'))
    all_done.add_done_callback(functools.partial(callback, n='B'))


async def main(all_done):
    await register_callbacks(all_done)
    print('设置future结果')
    all_done.set_result('结果')


event_loop = asyncio.get_event_loop()
try:
    all_done = asyncio.Future()
    event_loop.run_until_complete(main(all_done))
    print(all_done)
finally:
    event_loop.close()
