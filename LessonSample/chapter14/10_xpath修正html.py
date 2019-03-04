#!/usr/bin/python
# -*- coding: UTF-8 -*-
from io import StringIO

from lxml import etree

broken_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>王大拿拿大锤</title>
</head>
<body>
<p>锤子手机真锤子
<p><a href="http://www.163.com">网易
</body>
</html>
"""

html_root = etree.HTML(broken_html)
print etree.tostring(html_root, encoding="utf-8", pretty_print=True)

#parser = etree.HTMLParser()
#tree = etree.parse(StringIO(broken_html.decode("utf-8")), parser)
#print etree.tostring(tree, encoding="utf-8", pretty_print=True, method="html")
