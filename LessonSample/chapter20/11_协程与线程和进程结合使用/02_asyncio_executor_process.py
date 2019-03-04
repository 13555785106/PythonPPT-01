import asyncio
import concurrent.futures
import logging
import sys
import time


def blocks(n):
    log = logging.getLogger('blocks({})'.format(n))
    log.info('运行')
    time.sleep(n)
    log.info('完成')
    return n ** 2


async def run_blocking_tasks(executor):
    log = logging.getLogger('run_blocking_tasks')
    log.info('启动')

    log.info('创建执行者任务')
    loop = asyncio.get_event_loop()
    blocking_tasks = [loop.run_in_executor(executor, blocks, i) for i in range(1,10)]
    log.info('等待执行者任务')
    completed, pending = await asyncio.wait(blocking_tasks)
    results = [t.result() for t in completed]
    log.info('结果: {!r}'.format(results))

    log.info('退出')


if __name__ == '__main__':
    # 配置日志输出信息
    logging.basicConfig(
        level=logging.INFO,
        format='PID %(process)5s %(name)18s: %(message)s',
        stream=sys.stderr,
    )

    # 创建进程池
    executor = concurrent.futures.ProcessPoolExecutor(
        max_workers=3,
    )

    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(
            run_blocking_tasks(executor)
        )
    finally:
        event_loop.close()
