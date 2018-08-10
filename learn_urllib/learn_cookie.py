"""
    手动处理cookie
"""
import os
import webbrowser
from urllib import request

BASE_DIR = os.path.dirname(__file__)

login_url = 'http://www.renren.com/SysHome.do'
target_url = 'http://www.renren.com/880151247/profile/'

# 手动在请求头中添加cookie字段
headers = {
    'User-Agent': 'Mozilla/5.0',
    'Referer': 'http://www.baidu.com',
    'Cookie': 'anonymid=jkmezihttqs0a1; depovince=ZGQT; _r01_=1; _de=84A3A1CC7DEF8A2D3CE9293FC95F4D3A5212E40F3D18115C; ln_uact=gengwenhao97@126.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20120705/1025/h_main_2FwJ_2aa3000002441375.jpg; wp=0; jebecookies=702ec5a1-2f74-4213-862b-785da3295c47|||||; JSESSIONID=abc8urh7uyZtd_gNDCIuw; ick_login=e0f21613-efee-47aa-ac68-5a4329cebb8d; p=223204de22a9c1f497a53f690482b03f6; first_login_flag=1; t=8cef84e73a49154d56400d3a41e20a536; societyguester=8cef84e73a49154d56400d3a41e20a536; id=396330976; xnsid=dd853b5b; loginfrom=null; ver=7.0; wp_fold=0; XNESSESSIONID=abcnvmUF-aciY6izKFIuw'
}

req = request.Request(url=target_url, headers=headers)
resp = request.urlopen(req)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(resp.read().decode('utf-8'))
    webbrowser.open(os.path.join(BASE_DIR, 'index.html'))
