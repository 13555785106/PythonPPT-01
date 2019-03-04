import asyncio
import random


async def phase(c):
    # 随机休眠一定的秒数
    seconds = random.randint(1, 10)
    print('phase {} 执行，休眠 {} 秒'.format(c, seconds))
    await asyncio.sleep(seconds)
    print('phase {} 完成'.format(c))
    return 'phase {} 结果'.format(c)


async def main(chars):
    print('mian启动')
    phases = [phase(c) for c in chars]
    print('等待多个phase完成')
    # 会一直等待，不会存在未决的任务
    completed, pending = await asyncio.wait(phases)
    results = [t.result() for t in completed]
    print('结果: {!r}'.format(results))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main('ACBDEF'))
finally:
    event_loop.close()
