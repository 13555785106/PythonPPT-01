import asyncio


def callback(n):
    print('调用callback 参数是 {}'.format(n))


async def main(loop):
    print('注册回调')
    loop.call_later(2, callback, 'C')
    loop.call_later(1, callback, 'B')
    loop.call_soon(callback, 'A')

    await asyncio.sleep(3)


event_loop = asyncio.get_event_loop()
try:
    print('进入事件循环')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('关闭事件循环')
    event_loop.close()
