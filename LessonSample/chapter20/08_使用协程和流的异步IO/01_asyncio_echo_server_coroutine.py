import asyncio
import logging
import sys


async def echo(reader, writer):
    address = writer.get_extra_info('peername')
    log = logging.getLogger('echo_{}_{}'.format(*address))
    log.debug('connection accepted')
    while True:
        data = await reader.read(128)
        if data:
            log.debug('收到:{!r}'.format(data))
            writer.write(data)
            await writer.drain()
            log.debug('发送:{!r}'.format(data))
        else:
            log.debug('关闭')
            writer.close()
            return

SERVER_ADDRESS = ('localhost', 10000)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s: %(message)s',
    stream=sys.stderr,
)
log = logging.getLogger('main')

event_loop = asyncio.get_event_loop()
factory = asyncio.start_server(echo, *SERVER_ADDRESS)
server = event_loop.run_until_complete(factory)
log.debug('启动服务器 ip={},port={}'.format(*SERVER_ADDRESS))
# Enter the event loop permanently to handle all connections.
try:
    event_loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    log.debug('关闭服务器')
    server.close()
    event_loop.run_until_complete(server.wait_closed())
    log.debug('关闭事件循环')
    event_loop.close()