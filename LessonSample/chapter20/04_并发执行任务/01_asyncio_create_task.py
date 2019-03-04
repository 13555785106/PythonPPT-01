import asyncio


async def task_func():
    print('task_func运行')
    return '结果'


async def main(loop):
    print('创建task')
    task = loop.create_task(task_func())
    print('等待 {!r}'.format(task))  # 此时task处于pending状态
    return_value = await task
    print('task 完成 {!r}'.format(task))  # 此时task处于finished状态
    print('返回值: {!r}'.format(return_value))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
