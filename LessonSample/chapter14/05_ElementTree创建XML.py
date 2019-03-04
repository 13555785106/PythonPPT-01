#!/usr/bin/python
# -*- coding: UTF-8 -*-

from xml.etree.ElementTree import Element, SubElement, ElementTree, tostring

# 生成根节点
html = Element('html')
# 生成第一个子节点 head
head = SubElement(html, 'head')
# head 节点的子节点
title = SubElement(head, 'title')
title.text = u'网易'
# 生成 root 的第二个子节点 body
body = SubElement(html, 'body')
# body 的内容
body.text = u'欢迎访问，请玩游戏吧'
tree = ElementTree(html)
print tostring(html, encoding='utf-8')

tree.write('new.xml', encoding='utf-8')
