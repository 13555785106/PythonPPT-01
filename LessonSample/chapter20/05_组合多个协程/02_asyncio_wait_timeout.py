import asyncio
import random


async def phase(c):
    seconds = random.randint(1, 10)
    print('phase {} 执行，休眠 {} 秒'.format(c, seconds))
    try:
        await asyncio.sleep(seconds)
    except asyncio.CancelledError:
        print('phase {} 被取消'.format(c))
        raise
    else:
        print('phase {} 完成'.format(c))
        return 'phase {} 结果'.format(c)


async def main(chars):
    print('main运行')
    phases = [phase(c) for c in chars]
    print('等待一个 phase 完成')
    # 等待5秒，超过5秒的处于未决状态
    completed, pending = await asyncio.wait(phases, timeout=5)
    print('{} 个完成， {} 个未决'.format(len(completed), len(pending), ))
    # 取消5秒未完成的任务
    if pending:
        print('任务取消中')
        for t in pending:
            t.cancel()
    print('main退出')


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main('ACBDEFGHIJKLMN'))
finally:
    event_loop.close()
