"""
    爬取拉勾网
"""
from urllib import request
from urllib import parse

# url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='


url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
}

data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
}
req = request.Request(url=url, headers=headers, method='POST',
                      data=parse.urlencode(data).encode('utf-8'))
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))
