#!/usr/bin/python
# -*- coding: UTF-8 -*-
import select
import socket

# 创建socket文件句柄
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置socket为ip address复用
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 将socket句柄绑定到本机的12345端口
server.bind(('0.0.0.0', 12345))
# 监听最大个数10个
server.listen(10)
# 设置非阻碍模式
server.setblocking(False)

# 创建一个poll对象
poll = select.poll()
print dir(poll)
# 注册socket文件句柄到 select.POLLIN点集
poll.register(server.fileno(), select.POLLIN)
# 测试代码不用鸟他
print 'server filno:', server.fileno()
# 创建字典来存储 连接 请求
connections = {}
requests = {}
responses = {}
while True:
    # 将epoll将发生改变的文件句柄回调到用户进程 用events暂存此数据
    events = poll.poll()
    # 将文件句柄 和 时间状态从events数据提出来 events = [(文件句柄,时间状态ID)]
    for fileno, event in events:
        # 判断是否为本地socket文件句柄 如果是说明第一次连接
        if fileno == server.fileno():
            # 等待客户端连接
            connection, addr = server.accept()
            # 取客户端的socket句柄整形比如 1 15 212
            connFd = connection.fileno()
            # 设置客户端socket为非阻碍模式
            connection.setblocking(False)
            # 将客户端socket句柄注册到EPOLLIN
            poll.register(connFd, select.POLLIN)
            # 将客户端socket句柄整形 和 客户端socket句柄放到connections字典暂存
            connections[connFd] = connection

        # 判断客户端是否断开连接
        elif event & select.POLLHUP:
            print('close')
            # 销毁已断开的客户端socket句柄整形的哦
            poll.unregister(fileno)
            # 关闭客户端socket连接
            connections[fileno].close()
            # 删除客户端暂存数据
            del connections[fileno]

        # 判断客户端是否为收
        elif event & select.POLLIN:
            # 接受数据 并strip掉没用的 比如：空格
            requests[fileno] = connections[fileno].recv(1024).strip()
            # 将客户端文件句柄整形的 从POLLIN中转移到 POLLOUT
            poll.modify(fileno, select.POLLOUT)

        # 判断客户端是否为发
        elif event & select.POLLOUT:
            # 发送数据
            connections[fileno].send(requests[fileno])
            # 将客户端文件句柄整形的 从POLLOUT中转移到 POLLIN
            poll.modify(fileno, select.POLLIN)
