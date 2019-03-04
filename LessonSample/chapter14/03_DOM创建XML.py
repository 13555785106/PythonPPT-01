#!/usr/bin/python
# -*- coding: UTF-8 -*-

from xml.dom.minidom import Document

doc = Document()  # 创建DOM文档对象
html = doc.createElement('html')

doc.appendChild(html)
head = doc.createElement('head')
head.appendChild(doc.createTextNode("网易"))
html.appendChild(head)
body = doc.createElement('body')
body.appendChild(doc.createTextNode("欢迎访问"))
html.appendChild(body)
print html.toxml()
f = open('163.xml', 'w')
doc.writexml(f, newl='\n', addindent='\t', encoding='utf-8')
f.close()
