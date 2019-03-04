import asyncio


def mark_done(future, result):
    print('future的结果设置为 {!r}'.format(result))
    future.set_result(result)


async def main(loop):
    all_done = asyncio.Future()
    print('分派 mark_done')
    loop.call_later(3,mark_done, all_done, '结果')
    print('等待结果...')
    result = await all_done
    print('返回的结果: {!r}'.format(result))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
