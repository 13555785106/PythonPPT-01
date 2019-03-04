import asyncio
import logging
import sys
async def echo_client(address, messages):
    log = logging.getLogger('echo_client')

    log.debug('连接到服务器 ip={},port={}'.format(*address))
    reader, writer = await asyncio.open_connection(*address)
    for msg in messages:
        writer.write(msg)
        log.debug('发送:{!r}'.format(msg))
    if writer.can_write_eof():
        writer.write_eof()
    await writer.drain()
    log.debug('等待回应')
    while True:
        data = await reader.read(128)
        if data:
            log.debug('收到:{!r}'.format(data))
        else:
            log.debug('关闭')
            writer.close()
            return


MESSAGES = [
    b'Apple',
    b'Banana',
    b'Peach',
]
SERVER_ADDRESS = ('localhost', 10000)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s: %(message)s',
    stream=sys.stderr,
)
log = logging.getLogger('main')

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(
        echo_client(SERVER_ADDRESS, MESSAGES)
    )
finally:
    log.debug('closing event loop')
    event_loop.close()