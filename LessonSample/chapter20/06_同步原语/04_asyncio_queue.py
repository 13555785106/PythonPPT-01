import asyncio


async def consumer(n, q):
    print('消费者 {}: 启动'.format(n))
    while True:
        print('消费者 {}: 等待 商品'.format(n))
        item = await q.get()
        print('消费者 {}: 得到 商品 {}'.format(n, item))
        if item is None:
            # None is the signal to stop.
            q.task_done()
            break
        else:
            await asyncio.sleep(1)
            q.task_done()
    print('消费者 {}: 结束'.format(n))


async def producer(q, chars):
    print('生产者: 启动')
    # 添加一些数字到队列来模拟工作
    for i in range(len(chars) * 3):
        await q.put("商品 %d" % i)
        print('生产者: 添加 商品{} 到队列'.format(i))
    # 添加None记录到队列通知消费者退出
    print('生产者: 添加结束信号到队列')
    for i in range(len(chars)):
        await q.put(None)
    print('生产者: 等待队列变空')
    await q.join()
    print('生产者: 结束')


async def main(loop, chars):
    # 创建一个固定大小的队列，生产者会阻塞知道消费者消费了一些商品
    q = asyncio.Queue(maxsize=len(chars))

    # 分派消费者任务
    consumers = [loop.create_task(consumer(c, q)) for c in chars]

    # 分派一个生产者任务
    prod = loop.create_task(producer(q, chars))

    # 等待所有协程完成
    await asyncio.wait(consumers + [prod])


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop, 'ABC'))
finally:
    event_loop.close()
