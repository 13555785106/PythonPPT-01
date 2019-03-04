import asyncio
import random


async def consumer(condition, n):
    async with condition:
        print('消费者 {} 正在等待'.format(n))
        await condition.wait()
        print('消费者 {} 结束'.format(n))


async def manipulate_condition(condition):
    await asyncio.sleep(3)

    for i in range(3):
        async with condition:
            num = random.randint(2, 5)
            print('通知 {} 个消费者'.format(num))
            condition.notify(n=num)
        await asyncio.sleep(3)

    async with condition:
        print('通知剩余消费者')
        condition.notify_all()


async def main(loop):
    # 创建一个条件
    condition = asyncio.Condition()

    # 设置观察条件的任务
    consumers = [consumer(condition, c) for c in "ABCDEFGHIJKLMN"]

    # 分派一个任务去操作条件变量

    loop.create_task(manipulate_condition(condition))

    # 等待消费者完成
    await asyncio.wait(consumers)


event_loop = asyncio.get_event_loop()
try:
    result = event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
