import asyncio


async def outer():
    print('协程outer运行')
    print('等待phase1结果')
    result1 = await phase1()
    print('等待phase2结果')
    result2 = await phase2(result1)
    return (result1, result2)


async def phase1():
    print('协程phase1运行')
    return 'phase1 结果'


async def phase2(arg):
    print('协程phase2运行')
    return 'phase2结果 源于 {}'.format(arg)


event_loop = asyncio.get_event_loop()
try:
    return_value = event_loop.run_until_complete(outer())
    print('返回值: {!r}'.format(return_value))
finally:
    event_loop.close()
