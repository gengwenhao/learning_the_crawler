"""
    学习requests中使用代理
"""
import requests

url = 'http://httpbin.org/ip'

proxy = {
    'http': '115.211.41.226:9000'
}

# 直接传入代理参数
resp = requests.get(url, proxies=proxy)
print(resp.status_code)
print(resp.reason)
print(resp.content)
print(resp.json())
