import asyncio
import functools


def unlock(lock):
    print('回调释放锁')
    lock.release()


async def coro1(lock):
    print('协程1等待锁')
    async with lock:
        print('协程1获取到锁')
    print('协程1释放锁')


async def coro2(lock):
    print('协程2等待锁')
    await lock.acquire()
    try:
        print('协程2获取到锁')
    finally:
        print('协程2释放锁')
        lock.release()


async def main(loop):
    # 创建并获取一个共享锁
    lock = asyncio.Lock()
    print('在启动协程之前请求锁')
    await lock.acquire()
    print('锁是否锁定: {}'.format(lock.locked()))

    # 分派一个回调去解锁
    loop.call_later(5, functools.partial(unlock, lock))

    # 运行使用锁的协程
    print('等待协程')
    await asyncio.wait([coro1(lock), coro2(lock)])


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
