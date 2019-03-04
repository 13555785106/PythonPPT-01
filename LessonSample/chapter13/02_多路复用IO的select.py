#!/usr/bin/python
# -*- coding: UTF-8 -*-
import select,socket
s = socket.socket()
host = socket.gethostname();port = 12345
s.bind((host, port));s.listen(5)
inputs = [s];outputs = [];errors = []
while True:
    # 需要监听的可读取、可写入及有异常的socket列表
    rs, ws, es = select.select(inputs, outputs, errors)
    for r in rs:
        if r is s:
            c, addr = s.accept();print '请求来自', addr
            inputs.append(c);outputs.append(c)
            errors.append(c)
        else:
            data = r.recv(1024)
            if data:
                print data
            else:
                if r in outputs:
                    outputs.remove(r)
                inputs.remove(r)
                r.close()
    for w in ws:
        w.sendall('你好,我来自服务器端!')
        inputs.remove(w)
        outputs.remove(w)
        errors.remove(w)
        w.close()

    for e in es:
        print '------', e
        inputs.remove(e)
        outputs.remove(e)
        errors.remove(e)
