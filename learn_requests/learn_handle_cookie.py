"""
    这里的session表示会话不是web后端存储用户状态的那个术语
"""
import os
import webbrowser

import requests

BASE_DIR = os.path.dirname(__file__)

# 创建一个会话
session = requests.session()
# 剩下的用法和requests直接调用一样
data = dict(
    log='gengwenhao97@126.com',
    pwd='13945657337xX',
)

session.post('http://www.gengwenhao.com/wp-login.php', data=data)
resp = session.get('http://www.gengwenhao.com/wp-admin/profile.php')
file_name = 'result.html'

with open(file_name, 'w', encoding='utf-8') as f:
    f.write(resp.text)
    webbrowser.open(os.path.join(BASE_DIR, file_name))
