#!/usr/bin/python
# -*- coding: UTF-8 -*-

from twisted.internet import reactor
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineOnlyReceiver


class ConnectionHandler(LineOnlyReceiver):

    def connectionMade(self):  # 连接成功
        self.num = 0
        self.sendLine('你说！我是谁啊？')

    def connectionLost(self, reason):  # 连接关闭
        pass

    def lineReceived(self, line):  # 收到数据
        print self.num, line
        self.sendLine(line)
        if self.num >= 9:
            self.transport.loseConnection()
        self.num += 1


class EchoClientFactory(ClientFactory):
    def startedConnecting(self, connector):  # 发起连接
        print connector

    def buildProtocol(self, addr):  # 连接完毕
        return ConnectionHandler()

    def clientConnectionLost(self, connector, reason):  # 连接关闭
        reactor.stop()

    def clientConnectionFailed(self, connector, reason):  # 连接失败
        reactor.stop()


reactor.connectTCP('localhost', 12345, EchoClientFactory())
reactor.run()
