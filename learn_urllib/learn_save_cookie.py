"""
    学习保存cookie MozillaCookieJar可以将cookie保存在本地并读取
"""
import functools
import os
import webbrowser
from http.cookiejar import MozillaCookieJar
from urllib import request
from urllib.parse import urlencode

BASE_DIR = os.path.dirname(__file__)

LOGIN_URL = 'http://www.gengwenhao.com/wp-login.php'

ADMIN_URL = 'http://www.gengwenhao.com/wp-admin/'

LOGIN_DATA = {
    'log': 'gengwenhao97@126.com',
    'pwd': '13945657337xX',
    'redirect_to': 'http://www.gengwenhao.com/wp-admin/',
    'rememberme': 'forever',
    'testcookie': 1,
    'wp-submit': '登录',
}

CUSTOMER_HEADERS = {
    'User-Agent': 'Mozilla/5.0',
    'Referer': 'http://www.baidu.com',
}

mozilla_cookie_jar = None


def save_cookie(wrap):
    @functools.wraps(wrap)
    def func(*args, **kwargs):
        result = wrap(*args, **kwargs)
        mozilla_cookie_jar.save()
        return result

    return func


def get_opener():
    global mozilla_cookie_jar
    mozilla_cookie_jar = MozillaCookieJar('cookie.txt')

    cookie_handler = request.HTTPCookieProcessor(mozilla_cookie_jar)

    _opener = request.build_opener(cookie_handler)
    return _opener


@save_cookie
def login(opener, login_url, login_data):
    data_bytes = urlencode(login_data).encode('utf-8')

    req = request.Request(
        url=login_url,
        data=data_bytes,
        method='POST'
    )

    _resp = opener.open(req)
    return _resp


def enter_admin_site(opener, admin_url, file_name='index.html'):
    _resp = opener.open(admin_url)
    with open(file_name, 'w', encoding='utf-8') as f:
        html_str = _resp.read().decode('utf-8')

        f.write(html_str)
        webbrowser.open(os.path.join(BASE_DIR, file_name))
    return _resp


def print_cookie():
    global mozilla_cookie_jar
    mozilla_cookie_jar = MozillaCookieJar('cookie.txt')

    mozilla_cookie_jar.load(ignore_discard=True)
    for cookie in mozilla_cookie_jar:
        print(cookie)


if __name__ == '__main__':
    opener = get_opener()

    login(opener, LOGIN_URL, LOGIN_DATA)
    enter_admin_site(opener, ADMIN_URL)
    print_cookie()
