import asyncio
import asyncio.subprocess


def _parse_results(output):
    print('解析结果')
    if not output:
        return []
    lines = output.splitlines()
    headers = lines[0].split()
    devices = lines[1:]
    results = [
        dict(zip(headers, line.split()))
        for line in devices
    ]
    return results


async def run_df():
    print('run_df运行')

    buffer = bytearray()

    create = asyncio.create_subprocess_exec(
        'df', '-hl',
        stdout=asyncio.subprocess.PIPE,
    )
    print('启动进程')
    proc = await create
    print('进程已经启动，pid:{}'.format(proc.pid))
    while True:
        line = await proc.stdout.readline()
        print('读取 {!r}'.format(line))
        if not line:
            print('命令已经无更多输出')
            break
        buffer.extend(line)
    print('等待进程结束')
    await proc.wait()
    return_code = proc.returncode
    print('返回码:{}'.format(return_code))
    if not return_code:
        cmd_output = bytes(buffer).decode()
        results = _parse_results(cmd_output)
    else:
        results = []

    return (return_code, results)


event_loop = asyncio.get_event_loop()
try:
    return_code, results = event_loop.run_until_complete(
        run_df()
    )
finally:
    event_loop.close()

if return_code:
    print('错误,返回码:{}'.format(return_code))
else:
    print('\nFree space:')
    for r in results:
        print('{Mounted:25}: {Avail}'.format(**r))
