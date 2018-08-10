"""
    处理不被信任的ssl证书
"""
import requests

# 设置verify参数为False不需要验证ssl证书
resp = requests.get('https://www.lthack.com', verify=False)
