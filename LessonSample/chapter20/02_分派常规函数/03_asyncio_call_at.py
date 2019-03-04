import asyncio
import time


def callback(n, loop):
    print('调用callback参数 {}，时间:{}'.format(n, loop.time()))


async def main(loop):
    now = loop.time()
    print('clock时间: {}'.format(time.time()))
    print('loop时间: {}'.format(now))

    print('注册callbacks')
    loop.call_at(now + 0.2, callback, 'C', loop)
    loop.call_at(now + 0.1, callback, 'B', loop)
    loop.call_soon(callback, 'A', loop)

    await asyncio.sleep(1)


event_loop = asyncio.get_event_loop()
try:
    print('进入事件循环')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('关闭事件循环')
    event_loop.close()
