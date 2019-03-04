#!/usr/bin/python
# -*- coding: UTF-8 -*-
from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):  # 处理开始标签
        # print('<%s>' % tag)
        if tag == 'a':
            # 判断标签<a>的属性
            for name, value in attrs:
                if name == 'href':
                    print '超链接地址:', value

    def handle_endtag(self, tag):  # 处理结束标签
        pass
        # print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        pass
        # print('<%s/>' % tag)

    def handle_data(self, data):
        if self.lasttag == 'a':
            self.lasttag = '???'
            print '超链接文本:', data

    def handle_comment(self, data):  # 处理注释
        print('<!-- -->')

    def handle_entityref(self, name):  # 处理一些特殊字符，以&开头的，比如
        print('&%s;' % name)

    def handle_charref(self, name):  # 处理特殊字符串，就是以&#开头的，一般是内码表示的字符
        print('&#%s;' % name)


html = '''<html>
<head>
<title>网易</title>
</head>
<body>
知名网站<br/>
<a href="http://www.apache.org">Apache</a>
<a href="http://www.microsoft.com">微软</a>
</body>
</html>'''
parser = MyHTMLParser()
parser.feed(html)
parser.close()
