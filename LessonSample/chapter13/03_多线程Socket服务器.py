#!/usr/bin/python
# -*- coding: UTF-8 -*-
from SocketServer import ThreadingTCPServer, StreamRequestHandler, threading


class Handler(StreamRequestHandler):

    def handle(self):
        print threading.current_thread().ident
        addr = self.request.getpeername()
        print self.rfile.readline()
        print '连接来自 ', addr

        self.wfile.write('欢迎你访问！')


server = ThreadingTCPServer(('', 12345), Handler)
print dir(server)
server.serve_forever()
