#!/usr/bin/python
# -*- coding: UTF-8 -*-
from lxml import etree

"""
XPath的基本语法知识： 
1) // 双斜杠 定位根节点，会对全文进行扫描，在文档中选取所有符合条件的内容，以列表的形式返回。 
2) / 单斜杠 寻找当前标签路径的下一层路径标签或者对当前路标签内容进行操作 
3) /text() 获取当前路径下的文本内容 
4) /@xxxx 提取当前路径下标签的属性值 
5) | 可选符 使用|可选取若干个路径 如//p | //div 即在当前路径下选取所有符合条件的p标签和div标签。 
6) . 点 用来选取当前节点 
7) .. 双点 选取当前节点的父节点 
"""
html_tree = etree.parse("movies.xml")
print html_tree
# print etree.tostring(html_tree, encoding="UTF-8")
print "1" * 64
for movie in html_tree.xpath("//movie"):
    print movie.get('title')
    for v in movie:
        print ' ' * 5, v.text

print "2" * 64
for year in html_tree.xpath("//movie/year/text()"):
    print year, type(year)

print "3" * 64
for src in html_tree.xpath("//movie/@src"):
    print src

print "4" * 64
for src in html_tree.xpath("//movie[contains(@src,'.com')]/@src"):
    print src

print "5" * 64
for src in html_tree.xpath("//movie[stars>8]/@src"):
    print src

print "6" * 64
for element in html_tree.xpath("movie/type/text()"):
    print element

print "7" * 64
for element in html_tree.xpath("movie[last()]/type/text()"):
    print element
