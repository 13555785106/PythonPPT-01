import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

url = "http://www.baidu.com/s?wd="
key="肖俊峰"
url+= urllib.request.quote(key)
req = urllib.request.Request(url)
htmlBytes = urllib.request.urlopen(url).read()
html = htmlBytes.decode(encoding='utf-8')
print(html)
