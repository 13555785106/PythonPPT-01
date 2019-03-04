import asyncio
import functools
import logging
import sys


class EchoClient(asyncio.Protocol):

    def __init__(self, messages, future):
        super().__init__()
        self.messages = messages
        self.log = logging.getLogger('EchoClient')
        self.f = future

    def connection_made(self, transport):
        print(type(transport))
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.log.debug(
            '连接到 IP={},PORT={}'.format(*self.address)
        )
        # This could be transport.writelines() except that
        # would make it harder to show each part of the message
        # being sent.
        for msg in self.messages:
            transport.write(msg)
            self.log.debug('发送:{!r}'.format(msg.decode("UTF-8")))
        if transport.can_write_eof():
            transport.write_eof()

    def data_received(self, data):
        self.log.debug('收到:{!r}'.format(data.decode("UTF-8")))

    def eof_received(self):
        self.log.debug('收到:EOF')
        self.transport.close()
        if not self.f.done():
            self.f.set_result(True)

    def connection_lost(self, exc):
        self.log.debug('服务器关闭了连接')
        self.transport.close()
        if not self.f.done():
            self.f.set_result(True)
        super().connection_lost(exc)


MESSAGES = [
    bytes('【第 1 条消息】', 'UTF8'),
    bytes('【第 2 条消息】', 'UTF8'),
    bytes('【第 3 条消息】', 'UTF8'),
]
SERVER_ADDRESS = ('localhost', 10000)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s: %(message)s',
    stream=sys.stderr,
)
log = logging.getLogger('main')

event_loop = asyncio.get_event_loop()

client_completed = asyncio.Future()

client_factory = functools.partial(
    EchoClient,
    messages=MESSAGES,
    future=client_completed,
)
factory_coroutine = event_loop.create_connection(
    client_factory,
    *SERVER_ADDRESS,
)
log.debug('等待客户端结束')
try:
    event_loop.run_until_complete(factory_coroutine)
    event_loop.run_until_complete(client_completed)
    print('-' * 128)
finally:
    log.debug('关闭事件循环')
    event_loop.close()
