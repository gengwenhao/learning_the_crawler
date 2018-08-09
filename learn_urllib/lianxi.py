from urllib import request

handler = request.ProxyHandler({
    'http': 'localhost:1080'
})

# 网络请求对象
opener = request.build_opener(handler)

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Referer': 'https://www.baidu.com/s?kw=lthack'
}

url = 'http://www.youtube.com'

req = request.Request(url=url, headers=headers)
resp = opener.open(req)
print(resp.read())
