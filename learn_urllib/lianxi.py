import os
import webbrowser
from http.cookiejar import MozillaCookieJar
from urllib import request
from urllib.parse import urlencode

BASE_DIR = os.path.dirname(__file__)

LOGIN_URL = 'http://www.gengwenhao.com/wp-login.php'

ADMIN_SITE_URL = 'http://www.gengwenhao.com/wp-admin/'

LOGIN_FORM_DATA = dict(
    log='gengwenhao97@126.com',
    pwd='13945657337xX',
)

MOZILLA_COOKIE_NAME = 'cookie.txt'

mozilla_cookie_jar = MozillaCookieJar(MOZILLA_COOKIE_NAME)


def load_local_cookie(*args, **kwargs):
    global mozilla_cookie_jar
    mozilla_cookie_jar.load(*args, **kwargs)


def save_local_cookie(*args, **kwargs):
    global mozilla_cookie_jar
    mozilla_cookie_jar.save(ignore_expires=True, ignore_discard=True)


def get_mozilla_cookie_opener(local_cookie=False):
    global mozilla_cookie_jar
    cookie_handler = request.HTTPCookieProcessor(mozilla_cookie_jar)
    local_cookie and load_local_cookie(ignore_expires=True, ignore_discard=True)
    _opener = request.build_opener(cookie_handler)
    return _opener


def login(opener, save_cookie=True):
    global mozilla_cookie_jar
    data_bytes = urlencode(LOGIN_FORM_DATA).encode('utf-8')

    req = request.Request(url=LOGIN_URL, data=data_bytes, method='POST')

    _resp = opener.open(req)
    save_cookie and save_local_cookie()
    return _resp


def enter_admi_site(opener, save_file_name='index.html'):
    _resp = opener.open(ADMIN_SITE_URL)

    html_str = _resp.read().decode('utf-8')
    with open(save_file_name, 'w', encoding='utf-8') as f:
        f.write(html_str)
        webbrowser.open(os.path.join(BASE_DIR, save_file_name))
    return _resp


if __name__ == '__main__':
    # 通过登录将cookie保存到本地
    opener = get_mozilla_cookie_opener(local_cookie=False)

    login(opener, save_cookie=True)
    enter_admi_site(opener)
    # 读取本地cookie跳过登录环节
    opener = get_mozilla_cookie_opener(local_cookie=True)

    enter_admi_site(opener)
