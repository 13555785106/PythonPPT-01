import asyncio


async def phase1():
    print('phase1运行')
    await asyncio.sleep(2)
    print('phase1完成')
    return 'phase1 结果'


async def phase2():
    print('phase2运行')
    await asyncio.sleep(1)
    print('phase2完成')
    return 'phase2 结果'


async def main():
    print('main开始')
    print('等待各个phase完成')
    results = await asyncio.gather(phase1(),phase2(),)
    print('最后的结果: {!r}'.format(results))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main())
finally:
    event_loop.close()