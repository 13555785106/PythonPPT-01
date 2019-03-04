import asyncio


async def coroutine():
    print('协程运行中')
    return '协程coroutine结果'


event_loop = asyncio.get_event_loop()
try:
    return_value = event_loop.run_until_complete(coroutine())
    print('返回: {!r}'.format(return_value))
finally:
    event_loop.close()
