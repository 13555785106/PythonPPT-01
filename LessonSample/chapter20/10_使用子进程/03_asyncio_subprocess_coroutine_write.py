import asyncio
import asyncio.subprocess


async def to_upper(input):
    print('开始to_upper')
    create = asyncio.create_subprocess_exec(
        'tr', '[:lower:]', '[:upper:]',
        stdout=asyncio.subprocess.PIPE,
        stdin=asyncio.subprocess.PIPE,
    )
    print('启动进程')
    proc = await create
    print('pid={}'.format(proc.pid))
    print('与进程开始通讯')
    stdout, stderr = await proc.communicate(input.encode())
    print('等待进程完成')
    await proc.wait()
    return_code = proc.returncode
    print('返回码:{}'.format(return_code))
    if not return_code:
        results = bytes(stdout).decode()
    else:
        results = ''

    return (return_code, results)


MESSAGE = """
This message will be converted
to all caps.
"""

event_loop = asyncio.get_event_loop()
try:
    return_code, results = event_loop.run_until_complete(
        to_upper(MESSAGE)
    )
finally:
    event_loop.close()

if return_code:
    print('错误，退出代码:{}'.format(return_code))
else:
    print('转换前信息: {!r}'.format(MESSAGE))
    print('转换后信息: {!r}'.format(results))

