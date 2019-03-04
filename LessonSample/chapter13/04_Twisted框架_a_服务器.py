#!/usr/bin/python
# -*- coding: UTF-8 -*-

from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver


class ConnectionHandler(LineReceiver):

    def connectionMade(self):
        print self.transport.client, '连接到服务器'

    def connectionLost(self, reason):
        print self.transport.client, '关闭'

    def lineReceived(self, line):
        print line
        self.sendLine(line)


factory = Factory()
factory.protocol = ConnectionHandler

reactor.listenTCP(12345, factory)
reactor.run()
