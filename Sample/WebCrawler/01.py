import os
import urllib.request

fileName = os.path.dirname(os.path.realpath(__file__)) + os.sep + "baidu.html"
file = urllib.request.urlopen("http://www.baidu.com")
print(dir(file))
print(file.getcode())
print(file.headers)
print(file.getheader("X-Ua-Compatible"))
#
htmlBytes = file.read()
html = htmlBytes.decode(encoding='utf-8')
# print(html)
file.close()
file = open(fileName, "wb")
file.write(htmlBytes)
file.close()
