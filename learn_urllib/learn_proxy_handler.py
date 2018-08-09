from urllib import request
from urllib import parse

url = 'http://ipinfo.io/ip'

# 使用代理
handler = request.ProxyHandler({
    'http': 'localhost:1080'
})

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Referer': 'https://www.baidu.com/s?kw=lthack'
}

opener = request.build_opener(handler)
req = request.Request(url=url)
resp = opener.open(req)
print(resp.read())
