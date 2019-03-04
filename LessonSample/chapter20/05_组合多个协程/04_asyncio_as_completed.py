import asyncio
import random
# python里怎么实现多个协程一起执行，只要完成一个就返回一个协程
# 需要使用新的函数as_completed()来实现，可以把多个并发的协程一起给它，
# 但它把返回的结果变成一个生成器，每次返回一个协程的结果，与函数wait()一样，
# 执行协程是乱序的，不会等所有协程执行完成才返回。

async def phase(c):
    seconds = random.randint(1, 10)
    print('phase {} 休眠 {} 秒'.format(c, seconds))
    await asyncio.sleep(seconds)
    print('phase {} 完成'.format(c))
    return 'phase {} 结果'.format(c)


async def main(chars):
    print('starting main')
    phases = [phase(v) for v in chars]
    print('等待所有phase完成')
    results = []
    for next_to_complete in asyncio.as_completed(phases):
        answer = await next_to_complete
        print('收到答案 {!r}'.format(answer))
        results.append(answer)
    print('结果: {!r}'.format(results))
    print('-'*128)
    return results


event_loop = asyncio.get_event_loop()
try:
    print(event_loop.run_until_complete(main('ABCDEFG')))
finally:
    event_loop.close()
