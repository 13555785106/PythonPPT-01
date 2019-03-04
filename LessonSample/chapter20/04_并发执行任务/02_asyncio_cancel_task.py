import asyncio


async def task_func():
    print('进入task_func')
    return '结果'


async def main(loop):
    print('创建任务')
    task = loop.create_task(task_func())
    print(dir(task))
    print('取消任务')
    task.cancel()

    print('被取消的任务 {!r}'.format(task))
    try:
        await task
    except asyncio.CancelledError:
        print('捕捉到被取消的任务')
    else:
        print('任务结果: {!r}'.format(task.result()))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
