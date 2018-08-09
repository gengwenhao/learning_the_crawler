"""
    request.urlopen 访问资源
    parse.urlencode url参数编码  dict -> str
    parse.parse_qs  url参数解码  str -> dict
    parse.urlsplit parse.urlparse 用于解析完整的url
"""
from urllib import request
from urllib import parse

# 访问页面 urlopen
# resp = request.urlopen('http://www.baidu.com')

# 下载文件 urlretrieve
# request.urlretrieve('http://www.baidu.com')

# 查询参数编码 urlencode (用于将查询dict拼装成query_string)
# params = {
#     'name': 'gengwenhao',
#     'age': '22',
#     'greet': 'hello',
# }
# result = parse.urlencode(params)
# print(result)
# params = parse.urlencode(dict(wd='学习python'))
# url = f'http://www.baidu.com/s?{params}'
# resp = request.urlopen(url)


# 查询参数解码 parse_qs (用于将query_string还原为查询参数dict)
# params = {
#     'name': '耿文浩',
#     'age': '22',
#     'greet': 'hello world',
# }
# qs = parse.urlencode(params)
# result = parse.parse_qs(qs)
# print(result)

# 解析完整url urlsplit 和 urlparse (两者用法基本相同 )
# url = 'http://www.baidu.com/s?wd=pyton&username=abc#1'
# result = parse.urlparse(url)
# result = parse.urlsplit(url)
# print(result)
# print('scheme:', result.scheme)
# print('netloc:', result.netloc)
# print('path:', result.path)
# print('query:', result.query)
# print('fragment:', result.fragment)
