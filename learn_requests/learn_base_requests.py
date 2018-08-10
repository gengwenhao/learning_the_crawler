"""
    学习requests库的基本使用
"""
import os
import webbrowser

import requests

BASE_DIR = os.path.dirname(__file__)


def requests_get():
    resp = requests.get('http://www.gengwenhao.com')
    # str
    print('text', resp.text)
    # bytes
    print('content', resp.content)
    # url
    print('url', resp.url)
    # encoding
    print('encoding', resp.encoding)
    # status_code
    print('status_code', resp.status_code)


def requests_get_with_query():
    params = {
        'wd': '如何学好Python'
    }
    headers = {
        'User-Agent': 'Mozila/5.0'
    }
    resp = requests.get('http://www.baidu.com/s', params=params, headers=headers)
    file_name = 'baidu.html'

    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(resp.content.decode('utf-8'))
        webbrowser.open(os.path.join(BASE_DIR, file_name))


def requests_post():
    data = dict(
        log='gengwenhao97@126.com',
        pwd='13945657337xX',
    )
    resp = requests.post('http://www.gengwenhao.com/wp-login.php', data=data)
    print(resp.status_code)
    print(resp.is_redirect)
    print(resp.text)


if __name__ == '__main__':
    # requests_get()
    # requests_get_with_query()
    requests_post()
