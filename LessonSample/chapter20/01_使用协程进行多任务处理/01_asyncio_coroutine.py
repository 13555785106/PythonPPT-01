import asyncio


async def coroutine():
    print('协程运行中')


event_loop = asyncio.get_event_loop()
try:
    print('启动协程')
    coro = coroutine()
    print(type(coro))
    print(dir(coro))
    print(coro.cr_running)
    print('进入事件循环')
    event_loop.run_until_complete(coro)
finally:
    print('关闭事件循环')
    event_loop.close()
