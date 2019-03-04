import asyncio


async def wrapped():
    print('wrapped运行')
    return '结果'


async def inner(task):
    print('inner: 开始')
    print('inner: 等待 {!r}'.format(task))
    result = await task
    print('inner: task 返回 {!r}'.format(result))


async def starter():
    print('starter: 创建task')
    task = asyncio.ensure_future(wrapped())
    print('starter: 等待 inner')
    await inner(task)
    print('starter: inner 返回')
    return '结果'


event_loop = asyncio.get_event_loop()
try:
    print('进入事件循环')
    result = event_loop.run_until_complete(starter())
    print(result)
finally:
    print('关闭事件循环')
    event_loop.close()
