"""
    使用代理的方法：
        使用ProxyHandler构建一个handler
        使用handler通过request.build_opener构建一个opener对象
        使用opener发起请求
"""
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

# 一个工厂函数
opener = request.build_opener(handler)
# 构建请求
req = request.Request(url=url)
# 发起请求
resp = opener.open(req)
print(resp.read())
