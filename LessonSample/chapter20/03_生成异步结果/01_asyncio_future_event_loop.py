import asyncio


def mark_done(future, result):
    print('future的结果设置为 {!r}'.format(result))
    future.set_result(result)


event_loop = asyncio.get_event_loop()
try:
    all_done = asyncio.Future()

    print('分派 mark_done')
    event_loop.call_soon(mark_done, all_done, '结果')

    print('进入事件循环')
    result = event_loop.run_until_complete(all_done)
    print('返回的结果: {!r}'.format(result))
finally:
    print('关闭事件循环')
    event_loop.close()

print('future中的结果 : {!r}'.format(all_done.result()))
