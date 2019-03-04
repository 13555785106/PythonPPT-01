import asyncio
import functools


def callback(arg, *, kwarg='默认值'):
    print('调用callback 参数是 {} 和 {}'.format(arg, kwarg))


async def main(loop):
    print('注册回调')
    loop.call_soon(callback, 'A')
    wrapped = functools.partial(callback, kwarg='赋了值')
    loop.call_soon(wrapped, 'B')

    await asyncio.sleep(1)


event_loop = asyncio.get_event_loop()
try:
    print('进入事件循环')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('关闭事件循环')
    event_loop.close()
