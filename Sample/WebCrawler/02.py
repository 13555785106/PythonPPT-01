import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://blog.csdn.net/rx3oyuyi/article/details/87529515"

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent',"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36")]

htmlBytes = opener.open(url).read()
html = htmlBytes.decode(encoding='utf-8')
print(html)
opener.close()
