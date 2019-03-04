import ssl
import urllib.request
import urllib.parse
url = "http://www.baidu.com/"
postData = urllib.parse.urlencode({"account":'sa',"password":"123"}).encode("UTF-8")
req = urllib.request.Request(url,postData)
htmlBytes = urllib.request.urlopen(url).read()
html = htmlBytes.decode(encoding='utf-8')
print(html)
