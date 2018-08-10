"""
    自动处理cookie
"""
import os
import webbrowser
from urllib import request
from http.cookiejar import CookieJar
from urllib.parse import urlencode

BASE_DIR = os.path.dirname(__file__)

# 登录地址
LOGIN_URL = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201875142656'

# 要访问地址
TARGET_URL = 'http://www.renren.com/880151247/profile/'

# 登录表单
LOGIN_FORM_DATA = dict(
    autoLogin=True,
    captcha_type='web_login',
    domain='renren.com',
    email='',
    f='http%3A%2F%2Fwww.renren.com%2F396330976',
    icode='点尺无短',
    key_id=1,
    origURL='http://www.renren.com/home',
    password='',
    rkey='e37cf7c04307ba10c1b50a9a887570ca',
)

# 通用请求头
DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0',
    'Referer': 'http://www.baidu.com',
}


def get_cookie_opener():
    """
        带cookie配置的opener
    :return:
    """
    # 创建cookiejar对象
    cookie_jar = CookieJar()

    # 使用coookiejar创建HTTPCookieProcess对象
    cookie_handler = request.HTTPCookieProcessor(cookie_jar)

    # 使用handler创建opener
    _opener = request.build_opener(cookie_handler)

    return _opener


def login_target_url(opener, form_data, login_url, headers):
    """
        登录保存cookie
    :param opener:
    :param form_data:
    :param login_url:
    :param headers:
    :return:
    """
    # 先url编码，之后utf8编码
    data_bytes = urlencode(form_data).encode('utf-8')

    req = request.Request(
        url=login_url,
        data=data_bytes,
        headers=headers,
        method='POST'
    )

    _resp = opener.open(req)

    return _resp


def visit_profile_site(opener, target_url):
    """
        通过cookie访问目标站点
    :param opener:
    :param target_url:
    :return:
    """
    # 访问目标站点
    _resp = opener.open(target_url)

    with open('index.html', 'w', encoding='utf-8') as f:
        html_str = _resp.read().decode('utf-8')
        f.write(html_str)
        webbrowser.open(os.path.join(BASE_DIR, 'index.html'))

    return _resp


if __name__ == '__main__':
    # 网络请求函数 opener
    opener_with_cookie = get_cookie_opener()
    # 登录
    login_target_url(opener_with_cookie, LOGIN_FORM_DATA, LOGIN_URL, DEFAULT_HEADERS)
    # 访问
    visit_profile_site(opener_with_cookie, TARGET_URL)
