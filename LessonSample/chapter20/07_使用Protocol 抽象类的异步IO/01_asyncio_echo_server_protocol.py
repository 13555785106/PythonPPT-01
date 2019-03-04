import asyncio
import logging
import sys


class EchoServer(asyncio.Protocol):
    def connection_made(self, transport):

        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.log = logging.getLogger(
            'EchoServer_{}_{}'.format(*self.address)
        )
        self.log.debug('connection accepted')

    def data_received(self, data):
        self.log.debug('收到: {!r}'.format(data.decode("UTF-8")))
        self.transport.write(data)
        self.log.debug('发送: {!r}'.format(data.decode("UTF-8")))

    def eof_received(self):
        self.log.debug('收到EOF')
        if self.transport.can_write_eof():
            self.transport.write_eof()

    def connection_lost(self, error):
        if error:
            self.log.error('ERROR: {}'.format(error))
        else:
            self.log.debug('正在关闭')
        super().connection_lost(error)


SERVER_ADDRESS = ('localhost', 10000)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s: %(message)s',
    stream=sys.stderr,
)
log = logging.getLogger('main')

event_loop = asyncio.get_event_loop()
factory = event_loop.create_server(EchoServer, *SERVER_ADDRESS)
server = event_loop.run_until_complete(factory)
log.debug('启动服务器 IP={},PORT={}'.format(*SERVER_ADDRESS))
try:
    event_loop.run_forever()
finally:
    log.debug('关闭服务器')
    server.close()
    event_loop.run_until_complete(server.wait_closed())
    log.debug('关闭事件循环')
    event_loop.close()
