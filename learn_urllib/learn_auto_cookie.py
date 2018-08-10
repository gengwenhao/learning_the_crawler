"""
    自动处理cookie
"""
import os
import webbrowser
from urllib import request
from http.cookiejar import CookieJar
from urllib.parse import urlencode

BASE_DIR = os.path.dirname(__file__)

login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201875142656'
target_url = 'http://www.renren.com/880151247/profile/'

# 手动在请求头中添加cookie字段
headers = {
    'User-Agent': 'Mozilla/5.0',
    'Referer': 'http://www.baidu.com',
}

# 创建cookiejar对象
cookie_jar = CookieJar()

# 使用coookiejar创建HTTPCookieProcess对象
cookie_handler = request.HTTPCookieProcessor(cookie_jar)

# 使用handler创建opener
opener = request.build_opener(cookie_handler)

# 发送登录请求
login_data = dict(
    autoLogin=True,
    captcha_type='web_login',
    domain='renren.com',
    email='gengwenhao97@126.com',
    f='http%3A%2F%2Fwww.renren.com%2F396330976',
    icode='点尺无短',
    key_id=1,
    origURL='http://www.renren.com/home',
    password='30746ed326031d02c4c3a98ce25d5900ce80ad4807b80919847eaa596eb973e7',
    rkey='e37cf7c04307ba10c1b50a9a887570ca',
)
encode_login_data = urlencode(login_data).encode('utf-8')
req = request.Request(url=login_url, data=encode_login_data, headers=headers, method='POST')
opener.open(req)

# 访问目标站点
resp = opener.open(target_url)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(resp.read().decode('utf-8'))
    webbrowser.open(os.path.join(BASE_DIR, 'index.html'))
