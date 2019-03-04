import asyncio
import functools


def set_event(event):
    print('设置事件')
    event.set()


async def coro1(event):
    print('协程1等待事件')
    await event.wait()
    print('协程1完成')


async def coro2(event):
    print('协程2等待事件')
    await event.wait()
    print('协程2完成')


async def main(loop):
    # 创建一个共享事件
    event = asyncio.Event()
    print('事件开始状态: {}'.format(event.is_set()))
    loop.call_later(5, functools.partial(set_event, event))
    await asyncio.wait([coro1(event), coro2(event)])
    print('事件结束状态: {}'.format(event.is_set()))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
