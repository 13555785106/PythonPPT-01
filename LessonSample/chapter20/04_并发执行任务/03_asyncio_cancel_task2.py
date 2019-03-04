import asyncio


async def task_func():
    print('任务开始休眠')
    try:
        await asyncio.sleep(10)
    except asyncio.CancelledError:
        print('task_func被取消')
        raise
    return '结果'


def task_canceller(t):
    print('开始取消')
    t.cancel()
    print('任务被取消')


async def main(loop):
    print('创建任务')
    task = loop.create_task(task_func())
    loop.call_soon(task_canceller, task)
    try:
        await task
    except asyncio.CancelledError:
        print('main()函数也能看到任务被取消')


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
