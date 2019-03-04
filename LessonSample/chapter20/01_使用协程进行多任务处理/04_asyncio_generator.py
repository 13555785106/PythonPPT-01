import asyncio


# Python3.5之前可以使用装饰器及 yield from 关键字

@asyncio.coroutine
def outer():
    print('协程outer运行')
    print('等待phase1结果')
    result1 = yield from phase1()
    print('等待phase2结果')
    result2 = yield from phase2(result1)
    return (result1, result2)


@asyncio.coroutine
def phase1():
    print('协程phase1运行')
    return 'phase1 结果'


@asyncio.coroutine
def phase2(arg):
    print('协程phase2运行')
    return 'phase2结果 源自 {}'.format(arg)


event_loop = asyncio.get_event_loop()
try:
    return_value = event_loop.run_until_complete(outer())
    print('返回值: {!r}'.format(return_value))
finally:
    event_loop.close()



